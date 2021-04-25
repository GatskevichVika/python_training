from model.group import Group
import time

def test_edit_first_group(app):
    old_groups = app.group.get_group_list()
    app.group.edit(Group(name="Редактирование", header="существующей", footer="группы, которое надо сделать по заданию"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
