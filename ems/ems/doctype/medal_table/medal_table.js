// Copyright (c) 2022, RG and contributors
// For license information, please see license.txt

frappe.ui.form.on('Medal Table', {
	refresh: function(frm) {
		frm.fields_dict['team'].get_query = function(doc){
			return {
				filters: {
					"select_main_event": doc.main_event
				}
			}
		}
	}
});
