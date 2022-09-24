# Copyright (c) 2022, RG and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class SubEventFormat(Document):
    def autoname(self):
        self.name = self.sub_event + '- fixtures and results'
