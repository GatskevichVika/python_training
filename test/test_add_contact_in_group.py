from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_in_group(app):

    old_contact_list = db.get_contact_list()
    if len(old_contact_list) == 0:
        app.contact.create(Contact(firstname="test"))

    old_group_list = db.get_group_list()
    if len(old_group_list) == 0:
        app.group.create(Group(name="test"))

    new_group_list = db.get_group_list()
    group_list = db.get_group_list()
    number_of_contacts = db.get_contact_list()  # общее количество контактов

    def find_group_that_does_not_contain_all_contacts(group_list, number_of_contacts):
        for group in group_list:
            contact_in_group = db.get_contact_in_group(Group(id=group.id))
            if len(contact_in_group) < len(number_of_contacts):
                return group
            else:
                app.contact.create(Contact(firstname="test"))
                return group

    group = find_group_that_does_not_contain_all_contacts(group_list, number_of_contacts)
    old_contact_in_group = db.get_contact_in_group(Group(id=group.id))
    old_contact_not_in_group = db.get_contact_not_in_group(Group(id=group.id))

    contact = random.choice(old_contact_not_in_group).id
    app.contact.add_contact_to_group(id=contact, gr_id=group.id)

    new_contact_not_in_group = db.get_contact_not_in_group(Group(id=group.id))
    new_contact_in_group = db.get_contact_in_group(Group(id=group.id))
    assert len(old_contact_not_in_group) - 1 == len(new_contact_not_in_group)
    assert len(old_contact_in_group) + 1 == len(new_contact_in_group)



