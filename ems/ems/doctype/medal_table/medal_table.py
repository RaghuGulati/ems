# Copyright (c) 2022, RG and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MedalTable(Document):
    def autoname(self):
        self.name = self.team
        gold = 0
        silver = 0
        bronze = 0

        doc = frappe.db.get_list('SubEventWiseMedals')
        for i in range(0,len(doc)):
            curr_doc = frappe.get_doc('SubEventWiseMedals', doc[i]['name'])
            if curr_doc.select_main_event == self.main_event:
                gold_team = curr_doc.gold_medal
                if gold_team == self.team:
                    gold += 1
                    #print('gold', team, curr_doc.select_sub_event)
                silver_team = curr_doc.silver_medal
                if silver_team == self.team:
                    silver += 1
                    #print('silver', team, curr_doc.select_sub_event)
                bronze_team = curr_doc.bronze_medal
                if bronze_team == self.team:
                    bronze += 1
                    #print('bronze', team, curr_doc.select_sub_event)

        self.gold_medals = gold
        self.silver_medals = silver
        self.bronze_medals = bronze
