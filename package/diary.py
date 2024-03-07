from package.diary_entry import DiaryEntry
from package.diary_not_found import DiaryNotFoundException
from package.entry_not_found import EntryNotFoundException
from package.incorrect_password import IncorrectPasswordException


class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.entries = []
        self.is_locked = True
        self.number_of_entries = 0
        self.id_number = 0

    def unlock_diary(self, password: str):
        if self.password == password:
            self.is_locked = False
        elif self.password != password:
            raise IncorrectPasswordException("Incorrect password")

    def lock_diary(self):
        self.is_locked = True

    def is_locked(self):
        return self.is_locked

    def create_entry(self, title: str, body: str):
        id_number = self.generate_id_number()
        entry = DiaryEntry(id_number, title, body)
        self.entries.append(entry)
        self.id_number += 1
        self.number_of_entries += 1
        return entry

    def delete_entry(self, id_number: int):
        if not self.is_locked:
            entry = self.find_entry(id_number)
            self.entries.remove(entry)
            self.number_of_entries -= 1

    def find_entry(self, id_number: int):
        for entry in self.entries:
            if entry.get_id_number() == id_number:
                return entry
        raise EntryNotFoundException("No entry with that ID number")

    def update_entry(self, id_number: int, new_title: str, new_body: str):
        entry = self.find_entry(id_number)
        entry.set_title(new_title)
        entry.set_body(new_body)

    def get_number_of_entries(self):
        return self.number_of_entries

    def generate_id_number(self):
        id_number = self.id_number
        id_number += 1
        return id_number
