from __future__ import unicode_literals

import frappe

def get_context(context):
    pass

def on_submit():

    data_from_form = frappe.form_dict
    new_entry = frappe.get_doc({
        "doctype": "tabRatings",
        "name": data_from_form.get("name"),
        "показатель_1": data_from_form.get("показатель_1"),
        "показатель_2": data_from_form.get("показатель_2"),
        "показатель_3": data_from_form.get("показатель_3"),
        "показатель_4": data_from_form.get("показатель_4"),
        "показатель_5": data_from_form.get("показатель_5"),
        "показатель_6": data_from_form.get("показатель_6"),
        "показатель_7": data_from_form.get("показатель_7"),
        "показатель_8": data_from_form.get("показатель_8"),
        "показатель_9": data_from_form.get("показатель_9"),
        "показатель_10": data_from_form.get("показатель_10"),
        })
    new_entry.insert()

    frappe.local.response['type'] = 'redirect'
    frappe.local.response['location'] = '/second_page'
