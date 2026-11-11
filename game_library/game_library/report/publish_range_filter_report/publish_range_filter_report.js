// Copyright (c) 2026, Bianz and contributors
// For license information, please see license.txt

frappe.query_reports["Publish Range Filter Report"] = {
	"filters": [
		{
			"fieldname": "studio_name",
			"label": __("Studio Name"),
			"fieldtype": "Data",
		},
		{
			"fieldname": "start_date",
			"label": __("Published Start Date"),
			"fieldtype": "Date",
		},
		{
			"fieldname": "end_date",
			"label": __("Published End Date"),
			"fieldtype": "Date",
		},
	]
};
