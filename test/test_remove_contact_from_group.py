from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_in_group(app):

    # получить список контактов, если контактов нет создать контакт
    contact_list = db.get_contact_list()
    if len(contact_list) == 0:
        app.contact.create(Contact(firstname="test"))
    # получить список групп, если групп нет создать группу
    group_list = db.get_group_list()
    if len(group_list) == 0:
        app.group.create(Group(name="test"))

    # выбираем случайную группу из списка
    group = random.choice(group_list)
    # Проверяем какие контакты в нее входят
    contact_in_group = db.get_contact_in_group(Group(id=group.id))
    # Если в группе нет контактов - добавляем контакт в группу:
    if len(contact_in_group) == 0:
        contact = random.choice(contact_list)
        app.contact.add_contact_to_group(id=contact.id, gr_id=group.id)
    # Проверяем какие контакты в нее входят ещё раз
    contact_in_group_new = db.get_contact_in_group(Group(id=group.id))
    # выбрать контакт который надо удалить
    contact_del = random.choice(contact_in_group_new)
    # добавить контакт в группу
    app.contact.remove_contact_from_group(id=contact_del.id, gr_id=group.id)
