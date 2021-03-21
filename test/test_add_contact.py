# -*- coding: utf-8 -*-
from model.contact import Contact
import time

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Петр", middlename="Петрович", lastname="Петров", company="Петрострой",
                             mobile="7777777", email="petr@petr.ru"))
    app.session.logout()
    time.sleep(0.1)


