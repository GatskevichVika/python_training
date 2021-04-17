# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="test", middlename="test", lastname="test", company="test", mobile="test", email="test"))
    app.contact.modify_first_contact(Contact(firstname="Николай"))

def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="test", middlename="test", lastname="test", company="test", mobile="test", email="test"))
    app.contact.modify_first_contact(Contact(middlename="Николаевич"))

def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="test", middlename="test", lastname="test", company="test", mobile="test", email="test"))
    app.contact.modify_first_contact(Contact(lastname="Николаев"))
