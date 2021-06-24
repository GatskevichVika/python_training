from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

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
    # найти первую группу по id, точнее из списка всех групп выбрать первую
    group = group_list[0].id
    # найти контакты которые не входят в первую группу
    contact_not_in_group = db.get_contact_not_in_group(Group(id=group))
    # выбрать контакт который надо добавить в группу
    contact = contact_not_in_group[0].id
    # добавить контакт в группу
    app.contact.add_contact_to_group(id=contact, gr_id=group)


def remove_contact_from_group(app):
    pass
