import frappe

def get_context(context):
    db = frappe.db.get_list("Medal Table")
    context.team = db
    return context