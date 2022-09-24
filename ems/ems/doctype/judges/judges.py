# Copyright (c) 2022, RG and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Judges(Document):
    def autoname(self):
        self.name = str(1001 + frappe.db.count('Judges')) + '-' + self.name1

