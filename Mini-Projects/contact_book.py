contacts = {}

while True:

    print("\n----- Contact Book -----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact Added!")

    elif choice == "2":

        if len(contacts) == 0:
            print("No contacts found.")

        else:
            print("\nContacts:")
            for name in contacts:
                print(name, "-", contacts[name])

    elif choice == "3":
        search = input("Enter name to search: ")

        if search in contacts:
            print("Phone Number:", contacts[search])

        else:
            print("Contact not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
