import re

def test_notes_from_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address

    assert contact_from_home_page.contact_and_email == merge_phones_like_on_home_page(contact_from_edit_page)


def clear(s):
        return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work,
                                                                 contact.phone2,contact.email, contact.email2,
                                                                  contact.email3]))))

