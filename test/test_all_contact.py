
from model.contact import Contact

def test_contact_from_home_page(app, db):
    # получить список всех контаков на главной
    contact_from_home_page = app.contact.get_contact_list()

    # получить список всех контактов из БД
    contact_from_bd = db.get_contact_list()
    # сравнить списки
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_bd, key=Contact.id_or_max)


