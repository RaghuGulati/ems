// Copyright (c) 2022, RG and contributors
// For license information, please see license.txt

frappe.ui.form.on('SubEventWiseMedals', {
	refresh: function(frm) {
		frm.fields_dict["select_sub_event"].get_query = function(doc) {
			return {
				filters: {
					"event": doc.select_main_event
				}
			}
		}
	

		frm.fields_dict["gold_medal"].get_query = function(doc) {
			return {
				filters: {
					"select_main_event": doc.select_main_event
				}
			}
		}

		frm.fields_dict["silver_medal"].get_query = function(doc) {
			return {
				filters: {
					"select_main_event": doc.select_main_event
				}
			}
		}


		frm.fields_dict["bronze_medal"].get_query = function(doc) {
			return {
				filters: {
					"select_main_event": doc.select_main_event
				}
			}
		}
		

	}
});
