# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="test", lastname="test"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname="Николаев", firstname="Николай")

    contact.id = old_contacts[index].id
    contact.firstname = old_contacts[index].firstname
    contact.lastname = old_contacts[index].lastname
    app.contact.modify_contact_by_index(index, contact)

    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_contact_middlename(app):
#    if app.contact.count() == 0:
#        app.contact.create(
#            Contact(firstname="test",  lastname="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(middlename="Николаевич"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)

#def test_modify_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create(
 #           Contact(firstname="test", lastname="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(lastname="Николаев"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
