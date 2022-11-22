import frappe
import csv
from datetime import datetime

MainEvent = ['Intercollege Table Tennis Tournament 2022','30-11-2022','04-12-2022','Guru Nanak Stadium','Mr. ABC']
SubEvent = ['Intercollege Table Tennis Tournament 2022', "Men's Singles", 1, 1,	0, 'MSTEM', "1001-MSTR", "Refree", "MSTR", 'Intercollege Table Tennis Tournament-101', "1001-MSTU",	'Umpire', 'MSTU', 'Intercollege Table Tennis Tournament-101' ]


def insert_mainevent_data():
    doc = frappe.new_doc('MainEvent')
    doc.name1 = MainEvent[0]
    doc.start_date = datetime.strptime(MainEvent[1], '%d-%m-%Y').date()
    doc.end_date = datetime.strptime(MainEvent[2],'%d-%m-%Y').date()
    doc.venue = MainEvent[3]
    doc.event_manager = MainEvent[4]
    doc.insert()

def insert_subevent_data():
    doc = frappe.new_doc('SubEvent')
    doc.event = SubEvent[0]
    doc.sevent = SubEvent[1]
    doc.knockouts = SubEvent[2]
    doc.no_of_participants = SubEvent[3]
    doc.no_of_accompanists = SubEvent[4]
    doc.event_manager = SubEvent[5]
    #doc.judges[0].category = SubEvent[7]
    #doc.judges[0].name1 = SubEvent[8]
    #doc.judges[1].category = SubEvent[11]
    #doc.judges[1].name1 = SubEvent[12]
    doc.insert(
        ignore_permissions=True, # ignore write permissions during insert
        ignore_links=True, # ignore Link validation in the document
        ignore_if_duplicate=True, # dont insert if DuplicateEntryError is thrown
        ignore_mandatory=True
      )

    doc2 = frappe.get_doc("SubEvent","Intercollege Table Tennis Tournament 2022-101")
    doc2.append("judges", {
            "category": SubEvent[7],
            "name1": SubEvent[8],
        })

    doc2.append("judges", {
            "category": SubEvent[11],
            "name1": SubEvent[12],
        })

    doc2.save()

def after_install():
    insert_mainevent_data()	
    insert_subevent_data()
