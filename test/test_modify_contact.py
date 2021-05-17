# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="test", lastname="test"))

    old_contacts = db.get_contact_list()
    contact = Contact(lastname="Николаев", firstname="Николай", middlename="Николаевич")
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id)

    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()

    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
