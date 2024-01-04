class ContactBook:
    def __init__(self):
        self.contacts = []
    def addContact(self, new_contact):
        self.contacts.append(new_contact)
    def searchContact(self, name):
        for contact in self.contacts:
            if(contact.name.lower() == name.lower()):
                return contact
        return None
    def displayContact(self):
        if(len(self.contacts) == 0):
            print("No contacts found...!")
        else:
            print("Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Gmail: {contact.gmail}")
                print("----------------------------------------------------")
    def editContact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                phone = input("Enter phone number: ")
                contact.phone = phone
                gmail = input("Enter gmail id: ")
                contact.gmail = gmail
                print("\nContact updated...!")
                return
        print("\nContact not found...!")
    def removeContact(self, contact):
        self.contacts.remove(contact)
