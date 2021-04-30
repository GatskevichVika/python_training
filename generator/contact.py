from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", address="", lastname="", company="", home="",
                 mobile="", work="", phone2="", email="", email2="", email3="")] + [Contact(firstname=random_string("firstname", 10),
                                                                                          middlename=random_string("middlename", 20),
                                                                                          lastname=random_string("lastname", 20),
                                                                                          address=random_string("address", 20),
                                                                                          company=random_string("company", 10),
                                                                                          home=random_string("home", 5),
                                                                                          mobile=random_string("mobile", 5),
                                                                                          work=random_string("work", 10),
                                                                                          phone2=random_string("phone2", 10),
                                                                                          email=random_string("email", 10),
                                                                                          email2=random_string("email2", 10),
                                                                                          email3=random_string("email3", 10))

    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))