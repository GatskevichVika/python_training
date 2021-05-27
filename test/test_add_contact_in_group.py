
from model.group import Group
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    # проверить есть ли вообще группы
    Gr = db.get_group_list()
    print("Группы:")
    group_id = []
    # получить список ID групп
    for group in Gr:
        group_id.append(int(group.id))
    print(group_id)

    # проверить есть ли вообще контакты
    adress = db.get_contact_list()
    print("Контакты:")
    print(adress)
    adr_id = []
    for contact in adress:
        adr_id.append(int(contact.id))
    print("ID контактов:")
    print(adr_id)
    address_in_group = db.get_contact_in_group(Group(id=group_id[0]))
    print("Контакты в первой группе:")

    def test_add_contact_to_group(app):
        # сначала нужно обозначить группу для которой делается проверка
        #for gr_id in group_id:
        for index in range(len(group_id)):
            # проверить какие контакты входят в группу
            address_in_group = db.get_contact_in_group(Group(id=group_id[index]))
            for i in range(len(adr_id)):
                if adr_id[i] not in [address_in_group]:
                    id = adr_id[i]
                    gr_id = group_id[index]
                    app.contact.add_contact_to_group(id, gr_id, index)


finally:
    pass
