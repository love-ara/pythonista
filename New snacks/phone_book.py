from operator import itemgetter

class PhoneBook:

    def __init__(self):
        self.contacts = []

    def get_contact(self):
        return self.contacts

    def add_contact(self, name: str, phone_number: str):
        contact = {"name": name, "phone_number": phone_number}
        self.contacts.append(contact)
        return f"Contact '{name}' added successfully."

    def search_contact(self, name: str):
        searched_contact = []
        for contact in self.contacts:
            if contact["name"] == name:
                searched_contact.append(contact)
        if searched_contact:
            result = " "
            for contact in searched_contact:
                result += contact["name"] + "\n"+ contact["phone_number"] + "\n"
        else:
            result = f"Contact '{name}' not found in the phonebook."
        return result

    def display_contacts(self):
        all_contacts = ""
        for contact in sorted(self.contacts, key=itemgetter("name")):
            all_contacts += contact["name"] + ":\n" + contact["phone_number"] + "\n"
        if all_contacts:
            return "Phone Book" + "\n" + all_contacts
        else:
            return "No contacts available."

    def edit_contact(self, name: str, new_name: str, phone_number: str, new_phone_number: str):
        for contact in self.contacts:
            if contact["name"] == name:
                contact["name"] = new_name
                contact["phone_number"] = new_phone_number
                return f"Contact '{name}' edited successfully."

    def delete_contact(self, name: str, phone_number: str):
       # name = input("Enter the name to delete: ")
        for contact in self.contacts:
            if contact["name"] == name:
                self.contacts.remove(contact)
                return f"Contact '{name}' deleted successfully."







#     def main(self):
#         exit_program = False
#         while not exit_program:
#             print("1. Add Contact\n2. Search contact\n3. Display Contacts\n4. Edit Contact\n5. Delete Contact\n6. Exit")
#             choice = int(input("Enter your choice: "))
#             if choice == 1:
#                 print(self.add_contact('ARA', '02938420933'))
#             elif choice == 2:
#                 print(self.search_contact('ARA'))
#             elif choice == 3:
#                 print(self.display_contacts('ARA'))
#             elif choice == 4:
#                 print(self.edit_contact('ARA', 'Ayo', '02938420933', '1233'))
#             elif choice == 5:
#                 print(self.delete_contact('ARA', '02938420933'))
#             elif choice == 6:
#                 exit_program = True
#                 print("Exiting...")
#
#
#
# phone_book = PhoneBook()
# phone_book.main()
