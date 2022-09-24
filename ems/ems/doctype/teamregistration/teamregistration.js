// Copyright (c) 2022, RG and contributors
// For license information, please see license.txt

frappe.ui.form.on('TeamRegistration', {
	refresh: function(frm) {
		frm.fields_dict['select_sub_event'].grid.get_field('sub_event').get_query = function(doc){
			return{
				filters: {
					"event": doc.select_main_event
				}
			}
		}
	}
});
