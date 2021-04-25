from model.contact import Contact

def test_edit_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.edit(Contact(firstname="Иван", middlename="Иванович", lastname="Иванов", company="Иванстрой",
                             mobile="8888888", email="ivan@ivan.ru"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
