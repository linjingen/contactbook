#!/usr/bin/python
#Filename : contact.py

import sys,os,cPickle
class inf:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

def readdata(filename):
    if os.stat(filename).st_size > 0:
        f = file(filename)
        data = cPickle.load(f)
        f.close()
    else:
        return {}
    return data
def writedata(filename,data):
    f = file(filename, 'w')
    cPickle.dump(data,f)
    f.close()

contact = {}

if os.path.isfile("./contact.txt") == False:
    os.system("touch contact.txt")
            
if len(sys.argv) < 2:
    print 'No actions'
    sys.exit()
elif sys.argv[1] == 'append':
    contact = readdata("contact.txt")
    name = raw_input("Enter the name:")
    email = raw_input("Enter the email:")
    phone = raw_input("Enter the phone:")
    information = inf(name,email,phone)
    contact[name] = information
    writedata("contact.txt",contact)
    print "append was executed successfully"
elif sys.argv[1] == 'search':
    contact = readdata("contact.txt")
    name = raw_input("Enter the name you want:")
    if contact.has_key(name):
        information = contact[name]
        print "Name:",information.name
        print "Email:",information.email
        print "phone:",information.phone
    else:
        print "No %s in Contact book"%name
elif sys.argv[1] == 'delete':
    contact = readdata("contact.txt")
    name = raw_input("Enter the name you want to delete:")
    if contact.has_key(name):
        del contact[name]
        writedata("contact.txt",contact)
        print "contact of %s has been deleted"%name
    else:
        print "No %s in contact book"%name
elif sys.argv[1] == 'edit':
    contact = readdata("contact.txt")
    name = raw_input("Enter the name you want to edit:")
    if name in contact:
        print "Name:", contact[name].name
        print "Email:", contact[name].email
        contact[name].email = raw_input("Enter new email:")
        print "Phone:", contact[name].phone
        contact[name].phone = raw_input("Enter new phone:")
        writedata("contact.txt",contact)
    else:
        print "No %s in Contact book"%name
elif sys.argv[1] == 'help':
    print """\
    option: 1) append:add new contact
            2) search:look for existing contact
            3) delete:delete existing contact
            4) edit:edit existing contact
            5) help:display options
            6) version:display version of contact"""
elif sys.argv[1] == 'version':
    print "version 0.1"
else:
    print "Unknown option"
