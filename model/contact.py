from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, address=None, lastname=None, company=None,
                 mobile=None, email=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.address = address
        self.lastname = lastname
        self.company = company
        self.mobile = mobile
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
