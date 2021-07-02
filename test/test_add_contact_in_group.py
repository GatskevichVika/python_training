from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_in_group(app):

    # получить список контактов, если контактов нет создать контакт
    old_contact_list = db.get_contact_list()
    if len(old_contact_list) == 0:
        app.contact.create(Contact(firstname="test"))
    # получить список групп, если групп нет создать группу
    old_group_list = db.get_group_list()
    if len(old_group_list) == 0:
        app.group.create(Group(name="test"))
    # список всех групп
    new_group_list = db.get_group_list()
    # проверяем какие контакты не входят в группу
    for group in new_group_list:
        contact_not_in_group = db.get_contact_not_in_group(Group(id=group.id))
        if len(contact_not_in_group) == 0:
            app.contact.create(Contact(firstname="test"))
    old_contact_not_in_group = db.get_contact_not_in_group(Group(id=group.id))
    old_contact_in_group = db.get_contact_in_group(Group(id=group.id))
    contact = random.choice(old_contact_not_in_group).id
    app.contact.add_contact_to_group(id=contact, gr_id=group.id)
    new_contact_not_in_group = db.get_contact_not_in_group(Group(id=group.id))
    new_contact_in_group = db.get_contact_in_group(Group(id=group.id))

    assert len(old_contact_not_in_group) - 1 == len(new_contact_not_in_group)
    assert len(old_contact_in_group) + 1 == len(new_contact_in_group)

