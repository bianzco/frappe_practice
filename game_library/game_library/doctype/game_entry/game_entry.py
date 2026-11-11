# Copyright (c) 2026, Bianz and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class GameEntry(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		game_description: DF.LongText
		game_logo: DF.AttachImage | None
		game_name: DF.Data
		game_studio: DF.Link
		publishing_date: DF.Date
		score: DF.Rating
	# end: auto-generated types
	pass
