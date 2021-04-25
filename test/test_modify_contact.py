# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="test", middlename="test", lastname="test", company="test", mobile="test", email="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="Николай"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="test", middlename="test", lastname="test", company="test", mobile="test", email="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(middlename="Николаевич"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="test", middlename="test", lastname="test", company="test", mobile="test", email="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="Николаев"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
