import random
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

# подключаемся к базе через ORMFixture
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_in_group(app):

    # смотрим сколько контактов уже в группе
    old_list = len(db.get_contact_in_group(Group(id="80")))
    # добавляем контакт в группу
    app.contact.add_contact_to_group()
    # смотрим сколько стало контактов в группе
    new_list = len(db.get_contact_in_group(Group(id="80")))
    # проверяем что количество увеличилось на 1
    assert old_list + 1 == new_list

def test_delete_contact_from_group(app):
    # смотрим сколько контактов уже в группе
    old_list = len(db.get_contact_in_group(Group(id="80")))
    # удаляем контакт из группы
    app.contact.delete_contact_from_group()
    # смотрим сколько стало контактов в группе
    new_list = len(db.get_contact_in_group(Group(id="80")))
    # проверяем что количество увеличилось на 1
    assert old_list - 1 == new_list
