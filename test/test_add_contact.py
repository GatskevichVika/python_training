# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Петр", lastname="Петров", middlename="Петрович", address="Петрова 2", home="55555",
                      mobile="55555", work="55555", phone2="55555", company="Петр",
                      email="test@test.ru", email2="test@test.ru", email3="test@test.ru")

    app.contact.create(contact)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()

    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

