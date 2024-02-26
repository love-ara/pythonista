from package.diary import Diary


class User:
    def __init__(self):
        self.diary = Diary('username', 'password')

    @staticmethod
    def create_diary(username: str, password: str):
        Diary(username, password)

    def lock_diary(self):
        self.diary.lock_diary()

    @staticmethod
    def unlock_diary(self):
        self.diary.unlock_diary('password')

    def add_entry(self, title: str, body: str):
        self.diary.create_entry(title, body)

    def find_entry(self, id_number: int):
        return self.diary.find_entry(id_number)

    def update_entry(self, id_number: int, new_title: str, new_body: str):
        self.diary.update_entry(id_number, new_title, new_body)

    def delete_entry(self, id_number: int):
        self.diary.delete_entry(id_number)
