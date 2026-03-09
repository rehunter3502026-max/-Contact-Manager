contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts[name] = phone
    print("Contact added.")

def view_contacts():
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(name, "-", phone)

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Found:", contacts[name])
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\nContact Manager")
    print("1. Add")
    print("2. View")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
