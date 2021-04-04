from model.group import Group
import time

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="Редактирование", header="существующей", footer="группы, которое надо сделать по заданию"))
    app.session.logout()
