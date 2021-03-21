# -*- coding: utf-8 -*-
from model.group import Group
import time

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Группа", header="Которую", footer="Надо создать по заданию"))
    app.session.logout()
    time.sleep(0.1)

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
    time.sleep(0.1)
