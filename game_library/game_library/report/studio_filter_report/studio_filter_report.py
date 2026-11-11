# Copyright (c) 2026, Bianz and contributors
# For license information, please see license.txt

import frappe
from dateutil.relativedelta import relativedelta
from frappe import _
from frappe.query_builder import DocType
from frappe.utils import getdate, nowdate


def execute(filters=None):
	filters = filters or {}
	return get_columns(), get_data(filters)


def get_columns():
	return [
		{"fieldname": "studio_name", "label": _("Studio Name"), "fieldtype": "Data"},
		{"fieldname": "established_on", "label": _("Established On"), "fieldtype": "Date"},
		{"fieldname": "studio_age", "label": _("Studio Age"), "fieldtype": "Int"},
		{"fieldname": "game_name", "label": _("Game Name"), "fieldtype": "Data"},
		{"fieldname": "publish_date", "label": _("Publish Date"), "fieldtype": "Date"},
		{"fieldname": "game_age", "label": _("Game Age"), "fieldtype": "Int"},
		{"fieldname": "score", "label": _("Score"), "fieldtype": "score"},
	]


def get_data(filters):
	studios = DocType("Game Studio")
	titles = DocType("Studio Titles")
	games = DocType("Game Entry")

	query = (
		frappe.qb.from_(studios)
		.left_join(titles)
		.on((titles.parent == studios.name) & (titles.parenttype == "Game Studio"))
		.left_join(games)
		.on(games.name == titles.game_name)
		.select(
			studios.studio_name,
			studios.established_on,
			games.game_name,
			titles.publish_date,
			titles.score,
		)
		.orderby(studios.studio_name)
	)

	if filters.get("studio_name"):
		query = query.where(studios.studio_name.like(f"%{filters['studio_name']}%"))

	rows = query.run(as_dict=True)  # type: ignore

	today = getdate(nowdate())
	for row in rows:
		row["studio_age"] = (
			relativedelta(today, getdate(row.established_on)).years if row.established_on else 0
		)
		row["game_age"] = relativedelta(today, getdate(row.publish_date)).years if row.publish_date else 0

	return rows


def execute_snapshot_report(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for snapshot report. When 'Synced
	Report' is enabled in report, framework will call this method
	every time the report is refreshed or a filter is updated. It
	accepts the same filters as normal execute. But a utility method -
	get_latest_sync, is also imported.

	"""
	from frappe.database.duckdb.database import get_latest_sync

	columns = [
		{"fieldname": "studio_name", "label": _("Studio Name"), "fieldtype": "Data"},
	]
	data = []

	return columns, data
