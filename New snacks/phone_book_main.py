from phone_book import PhoneBook

phone_book1 = PhoneBook()
def main():
        exit_program = False
        while not exit_program:
            print("1. Add Contact\n2. Search contact\n3. Display Contacts\n4. Edit Contact\n5. Delete Contact\n6. Exit")
            choice = int(input("Enter an option : "))
            if choice == 1:
                name = input("Enter the name: ")
                phone_number = input("Enter the phone number: ")
                print(phone_book1.add_contact(name, phone_number))
            elif choice == 2:
                name = input("Enter the name to search: ")
                print(phone_book1.search_contact(name))
            elif choice == 3:
                print(phone_book1.display_contacts())
            elif choice == 4:
                name = input("Enter the name to edit: ")
                new_name = input("Enter the new name: ")
                phone_number = input("Enter the old number: ")
                new_phone_number = input("Enter the new phone number: ")
                print(phone_book1.edit_contact(name, new_name, phone_number, new_phone_number))
            elif choice == 5:
                name = input("Enter the name to delete: ")
                phone_number = input("Enter the old number: ")
                print(phone_book1.delete_contact(name, phone_number))
            elif choice == 6:
                exit_program = True
                print("Exiting...")




main()
