# Copyright (c) 2026, Bianz and contributors
# For license information, please see license.txt

import frappe
from dateutil.relativedelta import relativedelta
from frappe.model.document import Document
from frappe.utils import getdate, nowdate


class GameStudio(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from game_library.game_library.doctype.studio_titles.studio_titles import StudioTitles

		established_on: DF.Date
		studio_address: DF.Geolocation
		studio_logo: DF.AttachImage | None
		studio_name: DF.Data
		studio_titles: DF.Table[StudioTitles]
	# end: auto-generated types

	@property
	def studio_age(self):
		if not self.established_on:
			return 0
		return relativedelta(getdate(nowdate()), getdate(self.established_on)).years
