# Copyright (c) 2023, Mayur and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime
class SiteActivationDetails(Document):
	def validate(self):
		self.get_document()
	def get_document(self):
		value=frappe.get_doc('Site Master',self.s_name1)
		self.s_date1 = value.s_date
		if not value.active:
			current_datetime = now_datetime()
			current_date = current_datetime.date()
			self.d_date = current_date

			

