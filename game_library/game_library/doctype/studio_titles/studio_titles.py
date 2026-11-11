# Copyright (c) 2026, Bianz and contributors
# For license information, please see license.txt

import frappe
from dateutil.relativedelta import relativedelta
from frappe.model.document import Document
from frappe.utils import getdate, nowdate


class StudioTitles(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		game_name: DF.Link
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		publish_date: DF.Date
		score: DF.Rating
	# end: auto-generated types

	@property
	def game_age(self):
		if not self.publish_date:
			return 0
		return relativedelta(getdate(nowdate()), getdate(self.publish_date)).years
