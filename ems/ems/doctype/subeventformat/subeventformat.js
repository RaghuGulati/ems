// Copyright (c) 2022, RG and contributors
// For license information, please see license.txt

frappe.ui.form.on('SubEventFormat', {

refresh: function(frm) {
	
frm.fields_dict['sub_event'].get_query = function(doc) {
	return {
		filters: {
			"event": doc.select_main_event
		}
	}
}


frm.fields_dict['schedule'].grid.get_field('team_1').get_query = function(doc) {
	return {
		filters:{
			"select_main_event": doc.select_main_event
		}
	}
}

frm.fields_dict['schedule'].grid.get_field('team_2').get_query = function(doc) {
	return {
		filters:{
			"select_main_event": doc.select_main_event
		}
	}
}


frm.fields_dict.schedule.grid.update_docfield_property(
'winner', 'options', ['Team1','Team2']
);


	}
});








/*
cur_frm.fields_dict['schedule'].grid.get_field('Winner').get_query = function(doc) {
	return {
		filters:{
			"select_main_event": doc.select_main_event
		}
	}
}
*/





