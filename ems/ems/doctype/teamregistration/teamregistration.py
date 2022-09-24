# Copyright (c) 2022, RG and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class TeamRegistration(Document):
    def autoname(self):
        self.name = self.select_main_event + '-' + self.team_name

        for i in range(0,len(self.pdetails)):
            self.pdetails[i].team = self.name


        for j in range(0, len(self.tdetails)):
            self.tdetails[j].team = self.name


        for k in range(0, len(self.select_sub_event)):
            self.select_sub_event[k].team = self.name
