import re


from model.contact import Contact

def test_contact_from_home_page(app, db):
    # получить список всех контаков на главной
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    # получить список всех контактов из БД
    contact_from_bd = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contact_from_home_page)):

        assert contact_from_home_page[i].lastname == contact_from_bd[i].lastname
        assert contact_from_home_page[i].firstname == contact_from_bd[i].firstname
        assert contact_from_home_page[i].address == contact_from_bd[i].address
        assert contact_from_home_page[i].all_phones_from_home_page == merge_phones_like_from_home_page(
            contact_from_bd[i])
        assert contact_from_home_page[i].all_emails_from_home_page == merge_emails_like_from_home_page(
            contact_from_bd[i])

    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_bd, key=Contact.id_or_max)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                      [contact.home, contact.mobile, contact.work, contact.phone2]))))

def merge_emails_like_from_home_page(contact):
    return "\n".join([contact.email, contact.email2, contact.email3])
    #return "\n".join(filter(lambda x: x != "",
    #                        map(lambda x: clear(x),
    #                            filter(lambda x: x is not None,
    #                                  [contact.email, contact.email2, contact.email3]))))

