from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="Иван", middlename="Иванович", lastname="Иванов", company="Иванстрой",
                             mobile="8888888", email="ivan@ivan.ru"))
    app.session.logout()