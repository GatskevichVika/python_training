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
    new_contact_list = db.get_contact_list()
    new_group_list = db.get_group_list()
    # выбираем случайную группу из списка
    group = random.choice(new_group_list)
    # Проверяем какие контакты в нее не входят
    contact_not_in_group = db.get_contact_not_in_group(Group(id=group.id))
    # выбрать контакт который надо добавить в группу
    contact = random.choice(contact_not_in_group).id
    # добавить контакт в группу
    app.contact.add_contact_to_group(id=contact, gr_id=group.id)



