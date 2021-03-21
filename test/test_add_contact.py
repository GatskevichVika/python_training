# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Петр", middlename="Петрович", lastname="Петров", company="Петрострой",
                             mobile="7777777", email="petr@petr.ru"))
    app.session.logout()


