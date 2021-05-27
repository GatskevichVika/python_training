import random

from model.contact import Contact

def test_add_contact_in_group(app, db):
    old_contacts = db.get_contact_list()

    app.contact.add_contact_to_group()


    # открыть домашнюю страницу
    # выбрать группу в которую добавляю контакты
    # запросить в БД какие в группе контакты (контакт добавляется в группу по id)
    # выбрать контакт на главной странице
    # добавить контакт в выбранную группу
    # проверить в БД увеличилось ли кол-во контактов в этой группе

