// Copyright (c) 2024, kaushal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Appoinment', {
	refresh: function(frm) {
		frm.set_query('shift',(doc)=>{
			return{
				filters:{
					"clinic":doc.clinic
				}
			}
		})
	}
});
