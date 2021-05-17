from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, address=None, lastname=None, company=None, home=None,
                 mobile=None, work=None, phone2=None, email=None, id=None, contact_and_email=None,
                 all_phones_from_home_page=None, email2=None, email3=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.address = address
        self.lastname = lastname
        self.home = home
        self.mobile = mobile
        self.work = work
        self.phone2 = phone2
        self.company = company
        self.email = email
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.contact_and_email = contact_and_email

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
