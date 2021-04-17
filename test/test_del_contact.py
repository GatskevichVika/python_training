from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", company="test", mobile="test", email="test"))
    app.contact.delete_first_contact()

