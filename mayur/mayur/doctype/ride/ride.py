import frappe
from frappe.website.website_generator import WebsiteGenerator

class Ride(WebsiteGenerator):
	def validate(self):
		cd = self.cost_breakup
		thours = 0
		for i in cd:
			thours += i.hour
		
		self.total_hours = thours
		self.total_ammount = self.total_hours * self.rate_per_hour
	