from datetime import datetime


class DiaryEntry:
    def __init__(self, id_number: int, title: str, body: str):
        self.id_number = id_number
        self.body = body
        self.title = title
        self.created_at = datetime.now()

    def get_id_number(self):
        return self.id_number

    def set_body(self, body: str):
        self.body = body

    def set_title(self, title: str):
        self.title = title

    def get_body(self):
        return self.body

    def get_title(self):
        return self.title

    def __str__(self):
        return f'Date created: {self.created_at}\nID Number: {self.id_number}\nTitle: {self.title}\nBody: {self.body}'
