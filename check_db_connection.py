
from model.group import Group
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    #l = db.get_contact_not_in_group(Group(id="99"))
    group_list = db.get_group_list()
    #for item in group_list:
    print(group_list[0].id)
    #print(len(l))

    group = group_list[0].id
    # найти контакты которые не входят в первую группу
    contact_not_in_group = db.get_contact_not_in_group(Group(id=group))
    # выбрать контакт который надо добавить в группу
    contact = contact_not_in_group[0].id

    print(group)
    print(contact_not_in_group)
    print(contact)
finally:
    pass