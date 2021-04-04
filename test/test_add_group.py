# -*- coding: utf-8 -*-
from model.group import Group
import time

def test_add_group(app):
    app.group.create(Group(name="Группа", header="Которую", footer="Надо создать по заданию"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


