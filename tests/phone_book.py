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







