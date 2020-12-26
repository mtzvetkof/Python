import json


class Contacts:

    def __init__(self, name):
        self.name = name
        self.email = ''
        self.phone = ''

    def set_email(self, email):
        self.email = email
        return self.email

    def set_phone(self, phone):
        self.phone = phone
        return self.phone

    def contact_update(self, name, email, phone):
        if self.email == '':
            self.email = email
        if self.phone == '':
            self.phone = phone

    def __repr__(self):
        representation = [f'Name: {self.name}', f'e-mail: {self.email}', f'phone: {self.phone}']
        return ' / '.join(representation)


class Leads:
    def __init__(self):
        self.name = ''
        self.email = ''
        self.phone = ''

    def set_name(self, name):
        self.name = name
        return self.name

    def set_email(self, email):
        self.email = email
        return self.email

    def set_phone(self, phone):
        self.phone = phone
        return self.phone

    def contact_update(self, name, email, phone):
        if self.name == '':
            self.name = name
        if self.email == '':
            self.email = email
        if self.phone == '':
            self.phone = phone

    def __repr__(self):
        representation = [f'Name: {self.name}', f'e-mail: {self.email}', f'phone: {self.phone}']
        return ' / '.join(representation)


def find_contact_by_email(person_email, list):
    if not person_email == '':
        for object_person in list:
            if object_person.email == person_email:
                return object_person


def find_contact_by_phone(person_phone, list):
    if not person_phone == '':
        for object_person in list:
            if object_person.phone == person_phone:
                return object_person




def search_in_list(person, list):
    contact_found_by_email = find_contact_by_email(person['email'], list)
    if contact_found_by_email is not None:
        contact_found_by_email.contact_update(person['name'], person['email'], person['phone'])
        return contact_found_by_email
    contact_found_by_phone = find_contact_by_phone(person['phone'], list)
    if contact_found_by_phone is not None:
        contact_found_by_phone.contact_update(person['name'], person['email'], person['phone'])
        return contact_found_by_phone



contacts_list = []
leads_list = []
# We populate our contacts_list from file contacts.txt
file = open('contacts.txt', 'r')
Lines = file.readlines()
for line in Lines:
    line = line[:-1]
    name, email, phone = line.split(' / ')
    contact_object = Contacts(name)
    if not email == 'None':
        contact_object.set_email(email)
    if not phone == "None":
        contact_object.set_phone(phone)
    contacts_list.append(contact_object)

# Now we populate our leads_list from file leads.txt
file = open('leads.txt', 'r')
Lines = file.readlines()
for line in Lines:
    line = line[:-1]
    name, email, phone = line.split(' / ')
    lead_object = Leads()
    if not name == 'None':
        lead_object.set_name(name)
    if not email == 'None':
        lead_object.set_email(email)
    if not phone == "None":
        lead_object.set_phone(phone)
    leads_list.append(lead_object)

# We populate our registrants from a json file
with open('registrant.json') as f:

    registrants = json.load(f)

registrants_list = registrants['registrants']


for person in registrants_list:
    if not search_in_list(person, contacts_list):
        contact_found_in_leeds = search_in_list(person, leads_list)
        if not contact_found_in_leeds == None:
            leads_list.remove(contact_found_in_leeds)
            contacts_list.append(contact_found_in_leeds)
            continue
        new_contact = Contacts(person['name'])
        new_contact.set_email(person['email'])
        new_contact.set_phone(person['phone'])
        contacts_list.append(new_contact)

print('Contact list:')
for contact in contacts_list:
    print(contact)
print('Leads list:')
for lead in leads_list:
    print(lead)

