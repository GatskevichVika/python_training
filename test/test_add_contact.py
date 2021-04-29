# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", middlename="",address="", home="", mobile="", work="", phone2="",
                    company="", email="", email2="", email3="")] + \
           [Contact(firstname=random_string("firstname", 10),
            lastname=random_string("lastname", 20),
            middlename=random_string("middlename", 20),
            address=random_string("address", 5),
            home=random_string("home", 5),
            mobile=random_string("mobile", 5),
            work=random_string("work", 5),
            phone2=random_string("phone2", 5),
            company=random_string("company", 5),
            email=random_string("email", 5),
            email2=random_string("email2", 5),
            email3=random_string("email3", 5))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    #contact = Contact(firstname="Петр", lastname="Петров", middlename="Петрович", address="Петрова 2", home="55555",
                     # mobile="55555", work="55555", phone2="55555", company="Петр",
                     # email="test@test.ru", email2="test@test.ru", email3="test@test.ru")

    app.contact.create(contact)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()

    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

