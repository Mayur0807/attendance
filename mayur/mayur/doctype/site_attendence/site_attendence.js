// Copyright (c) 2023, Mayur and contributors
// For license information, please see license.txt
frappe.ui.form.on('Site Attendence', {
	refresh: function(frm) {
		frm.set_query('s_name', function() {
			return {
				filters: {
					"active": 1
				}
			};
		});
	}
});
