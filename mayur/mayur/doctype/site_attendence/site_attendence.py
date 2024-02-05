# import frappe
# from frappe.model.document import Document
# from datetime import datetime

# class SiteAttendence(Document):
#     def validate(self):
#         a_date = datetime.strptime(self.a_date, "%Y-%m-%d").date()
#         a_date1 = a_date.strftime("%Y-%m-%d")

#         smd = frappe.get_doc('Site Master', self.s_name)
#         s_date1 = smd.s_date.strftime("%Y-%m-%d")

#         if a_date1 < s_date1:
#             frappe.throw("Attendance date is wrong")

#         if self.duplicate_record():
#             frappe.throw("Duplicate attendance record found for the same site and date")

#         self.duplicate_workers()

#         for r in self.wa_table:
#             worker_details = frappe.get_doc('Worker Details', r.wa_id)
#             r.wa_name = worker_details.w_name
#             r.was_name = worker_details.ws_name
#             if worker_details.r_date and a_date < worker_details.r_date:
#                 frappe.throw("Attendance date cannot be earlier than the worker's registration date")

#     def duplicate_record(self):
#         filters = {
#             's_name': self.s_name,
#             'a_date': self.a_date
#         }
#         duplicate_exists = frappe.db.exists('Site Attendence', filters)
#         return duplicate_exists

#     def before_save(self):
#         self.worker_counts()

#     def worker_counts(self):    
#         total_workers = self.get_total_workers()
#         present_workers = len(self.wa_table) 
#         absent_workers = total_workers - present_workers
       
#         self.w_present = present_workers
#         self.w_total = total_workers
#         self.w_absent = absent_workers

#     def get_total_workers(self):

#         total_workers = frappe.db.count('Worker Details', filters={'ws_name': self.s_name})
#         return total_workers

#     def duplicate_workers(self):
#         worker_ids = set()
#         for wa in self.wa_table:
#             if wa.wa_id in worker_ids:
#                 frappe.throw(f"Duplicate worker found with ID {wa.wa_id} in Worker Attendance table.")
#             else:
#                 worker_ids.add(wa.wa_id)
import frappe
from frappe.model.document import Document
from datetime import datetime

class SiteAttendence(Document):
    def validate(self):
        a_date = datetime.strptime(self.a_date, "%Y-%m-%d").date()
        a_date1 = a_date.strftime("%Y-%m-%d")

        smd = frappe.get_doc('Site Master', self.s_name)
        s_date1 = smd.s_date.strftime("%Y-%m-%d")

        if a_date1 < s_date1:
            frappe.throw("Attendance date is wrong")

        if self.duplicate_record():
            frappe.throw("Duplicate attendance record found for the same site and date")

        self.duplicate_workers()

        for r in self.wa_table:
            worker_details = frappe.get_doc('Worker Details', r.wa_id)
            r.wa_name = worker_details.w_name
            r.was_name = worker_details.ws_name
            if worker_details.r_date and a_date < worker_details.r_date:
                frappe.throw("Attendance date cannot be earlier than the worker's registration date")

    def duplicate_record(self):
        filters = {
            's_name': self.s_name,
            'a_date': self.a_date
        }
        duplicate_exists = frappe.db.exists('Site Attendence', filters)
        return duplicate_exists

    def before_save(self):
        self.worker_counts()

    def worker_counts(self):    
        total_workers = self.get_total_workers()
        present_workers = len(self.wa_table) 
        absent_workers = total_workers - present_workers
       
        self.w_present = present_workers
        self.w_total = total_workers
        self.w_absent = absent_workers

    def get_total_workers(self):

        total_workers = frappe.db.count('Worker Details', filters={'ws_name': self.s_name})
        return total_workers

    def duplicate_workers(self):
        worker_ids = set()
        for wa in self.wa_table:
            if wa.wa_id in worker_ids:
                frappe.throw(f"Duplicate worker found with ID {wa.wa_id} in Worker Attendance table.")
            else:
                worker_ids.add(wa.wa_id)