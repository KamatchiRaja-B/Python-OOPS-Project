from Contact import *
from ContactBook import *
def main():
    contact_book = ContactBook()
    print("****************************************************")
    print("Contact book")
    print("Choices: \n1. Add contact")
    print("2. Search contact")
    print("3. Display contact")
    print("4. Edit contact")
    print("5. Remove contact")
    print("6. Exit")
    while True:
        print("****************************************************")
        choice = input("Enter your choice: ")
        if(choice == "1"):
            # Add contact
            print("****************************************************")
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            gmail = input("Enter gmail id: ")
            new_contact = Contact(name, phone, gmail)
            contact_book.addContact(new_contact)
            print("\nContact added successfully")
        elif(choice == "2"):
            # Search contact
            print("****************************************************")
            name = input("Enter name: ")
            contact = contact_book.searchContact(name)
            if(contact):
                print("\nContact found: ")
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Gmail: {contact.gmail}")
            else:
                print("\nContact not found...!")
        elif(choice == "3"):
            # Display contact
            print("****************************************************")
            contact_book.displayContact()
        elif choice == "4":
            # Edit contact
            print("****************************************************")
            name = input("Enter the contact name to be edited: ")
            contact_book.editContact(name)
        elif(choice == "5"):
            # Remove contact
            print("****************************************************")
            name = input("Enter the contact to be removed: ")
            contact = contact_book.searchContact(name)
            if(contact):
                contact_book.removeContact(contact)
                print("\nContact removed successfully...!")
            else:
                print("\nContact not found...!")
        elif choice == "6":
            # Exit contact
            print("****************************************************")
            print("Exiting the Contact book. Goodbye!")
            break
        else:
            print("****************************************************")
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
