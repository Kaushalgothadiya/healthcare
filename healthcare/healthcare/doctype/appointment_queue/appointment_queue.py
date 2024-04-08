# Copyright (c) 2024, kaushal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import frappe.utils

class AppointmentQueue(Document):
	pass


def create_queue_for_today(self):
	clinics=frappe.get_all("Clinic",filters={'is_published':True},pluck='name')
	

	for clinic in clinics:
		shifts=frappe.get_all("Schedule Shifts",filters={'clinic':clinic},pluck='name')
		for shift in shifts:
			frappe.get_doc(
				{
					"doctype":"Appointment Queue",
					"clinic":clinic,
					"date":frappe.utils.today(),
					"shift":shift
				}
			)
