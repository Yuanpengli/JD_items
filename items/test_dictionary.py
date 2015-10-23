__author__ = 'liyuanpeng'

Alice={}

Alice['phone'] = 2441
Alice['address'] = "foo daw"

Beth = {}
Beth['phone'] = 3424
Beth['address'] = "sfassds s daw"

Cecil = {}
Cecil['phone'] = 342324
Cecil['address'] = "ss ass sadw"

people = {}
people['Alice'] = Alice

people['Beth'] = Beth

people['Cecil'] = Cecil

label = {'phone':'phone number','address':'address'}

name = raw_input('name:')
request = raw_input ("phone number (p) or address(a):")

if request == "p":
    key = 'phone'
if request == 'a':
    key = 'address'

if name in people:
    print "%s's %s is %s." % (name, label[key],people[name][key])


#print people