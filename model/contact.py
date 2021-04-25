class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, company=None, mobile=None, email=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.company = company
        self.mobile = mobile
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return self.id == other.id and self.firstname == other.name
