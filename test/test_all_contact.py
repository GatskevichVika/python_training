import re
import random

from model.contact import Contact

def test_contact_from_home_page(app, db):
    # получить список всех контаков на главной
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    # получить список всех контактов из БД
    contact_from_bd = sorted(db.get_contact_list(), key=Contact.id_or_max)
    index = 0
    for row in contact_from_home_page:
        assert contact_from_home_page[index] == contact_from_bd[index]

        #assert contact_from_home_page[index].lastname == contact_from_bd[index].lastname
        #assert contact_from_home_page[index].firstname == contact_from_bd[index].firstname
        #assert contact_from_home_page[index].address == contact_from_bd[index].address
        #assert contact_from_home_page[index].all_phones_from_home_page == merge_phones_like_from_home_page(
            #contact_from_bd[index])
        #assert contact_from_home_page[index].all_emails_from_home_page == merge_emails_like_from_home_page(
            #contact_from_bd[index])
    index = index + 1


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                      [contact.home, contact.mobile, contact.work, contact.phone2]))))

def merge_emails_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                      [contact.email, contact.email2, contact.email3]))))

