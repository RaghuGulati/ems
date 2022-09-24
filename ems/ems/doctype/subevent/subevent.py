# Copyright (c) 2022, RG and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SubEvent(Document):
    def autoname(self):
        self.name = self.event + '-' + str(101 + frappe.db.count('SubEvent'))
        #self.test = self.name    

        for i in range(0, len(self.judges)):
            self.judges[i].sub_event = self.name


