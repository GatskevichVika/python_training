from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, address=None, lastname=None, company=None, homephone = None,
                 mobilephone=None, workphone=None, secondaryphone=None, email=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.address = address
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.company = company
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
