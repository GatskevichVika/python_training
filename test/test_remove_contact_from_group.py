from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_remove_contact_from_group(app):
    # Проверки предусловий:
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
    # запросить контакты которые входят в эту группу
    contact_in_group = db.get_contact_in_group(Group(id=group))
    # выбрать контакт который надо удалить из группы
    contact = contact_in_group[0].id
    # удалить контакт из группы
    app.contact.remove_contact_from_group(id=contact, gr_id=group)


    # выбрать группу в меню
    # выбрать контакты которые входят в группу
    # удалить первый контакт который входит в группу