# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(firstname="Петр", middlename="Петрович", lastname="Петров", company="Петрострой",
                             mobile="7777777", email="petr@petr.ru"))
