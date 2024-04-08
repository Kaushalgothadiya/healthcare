# Copyright (c) 2024, kaushal and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Doctor(Document):
	def validate(self):
		if self.last_name is not None:
			self.full_name=self.first_name+" "+self.last_name 
		else:
			self.full_name=self.first_name
