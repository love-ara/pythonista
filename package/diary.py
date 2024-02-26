from package.diary_entry import DiaryEntry


class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.entries = []
        self.isLocked = True
        self.number_of_entries = 0
        self.__id_number = 0
        self.len = self.number_of_entries

    def unlock_diary(self, password: str):
        if self.password == password:
            self.isLocked = False

    def lock_diary(self):
        self.isLocked = True

    def is_locked(self):
        return self.isLocked

    def create_entry(self, title: str, body: str):
        if not self.isLocked:
            id_number = self.__generate_id_number()
            entry = (id_number, title, body)
            self.entries.append(entry)
            self.number_of_entries += 1

    def delete_entry(self, id_number: int):
        if not self.isLocked:
            for entry in self.entries:
                if entry == self.find_entry(id_number):
                    self.entries.remove(entry)
                    self.__id_number -= 1
                    self.number_of_entries -= 1

    def find_entry(self, id_number: int):
        if not self.isLocked:
            for entry in self.entries:
                if self.__id_number == id_number:
                    return entry
            return None

    def update_entry(self, id_number: int, new_title: str, new_body: str):
        if not self.isLocked:
            if id_number in self.entries:
                entry = DiaryEntry(new_title, new_body)
                self.entries.append(entry)

    def get_number_of_entry(self):
        return self.number_of_entries

    def get_id_number(self, title: str):
        for entry in self.entries:
            self.__id_number = self.get_id_number(title)
            return self.__id_number

    def __generate_id_number(self):
        self.__id_number += 1
        return self.__id_number
