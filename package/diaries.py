from package.diary import Diary


class Diaries:
    def __init__(self):
        self.diaries = []

    def add_diary(self, username: str, password: str):
        diary = Diary(username, password)
        self.diaries.append(diary)

    def delete_diary(self, username: str, password: str):
        for diary in self.diaries:
            if username == diary.get_username() and password == diary.get_password():
                self.diaries.remove(diary)

    def find_by_username(self, username: str):
        for diary in self.diaries:
            if username == diary.get_username:
                return diary
        return None
