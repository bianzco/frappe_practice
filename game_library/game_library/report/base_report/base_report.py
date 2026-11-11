# Copyright (c) 2026, Bianz and contributors
# For license information, please see license.txt

import frappe
from dateutil.relativedelta import relativedelta
from frappe import _
from frappe.utils import getdate, nowdate


def execute(filters=None):
	return get_columns(), get_data()


def get_columns():
	return [
		{"fieldname": "studio_name", "label": _("Studio Name"), "fieldtype": "Data"},
		{"fieldname": "established_on", "label": _("Established On"), "fieldtype": "Date"},
		{"fieldname": "studio_age", "label": _("Studio Age"), "fieldtype": "Int"},
	]


def get_data():
	studios = frappe.get_all(
		"Game Studio",
		fields=["studio_name", "established_on"],
		order_by="studio_name asc",
	)

	today = getdate(nowdate())
	for studio in studios:
		studio["studio_age"] = (
			relativedelta(today, getdate(studio.established_on)).years if studio.established_on else 0
		)

	return studios


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
