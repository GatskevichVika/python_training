# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import random

def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="test", lastname="test"))

    old_contacts = db.get_contact_list()

    contact = random.choice(old_contacts)

    new_contact = Contact(lastname="Николаев", firstname="Николай", middlename="Николаевич")

    app.contact.modify_contact_by_id(contact.id, new_contact)

    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

