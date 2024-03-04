import unittest

from package.diary import Diary
from package.entry_not_found import EntryNotFoundException
from package.incorrect_password import IncorrectPasswordException


class TestDiary(unittest.TestCase):
    def setUp(self):
        self.diary = Diary('username', 'password')

    def test_diary_is_locked(self):
        self.assertTrue(self.diary.is_locked)

    def test_diary_is_be_unlocked(self):
        self.assertTrue(self.diary.is_locked)
        self.diary.unlock_diary('password')
        self.assertFalse(self.diary.is_locked)

    def test_entry_can_be_created(self):
        self.assertTrue(self.diary.is_locked)
        self.diary.unlock_diary('password')
        self.diary.create_entry('title', 'body')
        self.assertEqual(1, len(self.diary.entries))

    def test_entry_can_be_deleted(self):
        self.assertTrue(self.diary.is_locked)
        self.diary.unlock_diary('password')
        self.diary.create_entry('title', 'body')
        self.diary.create_entry('new_title', 'body')

        self.assertEqual(2, self.diary.get_number_of_entries())

        self.diary.delete_entry(2)

        self.assertEqual(1, self.diary.get_number_of_entries())

    def test_entry_can_be_updated(self):
        self.assertTrue(self.diary.is_locked)
        self.diary.unlock_diary('password')
        self.diary.create_entry("title", "body")
        entry = self.diary.update_entry(1, "new_title", "body")
        self.assertEqual(entry, self.diary.update_entry(1, "new_title", "body"))

    def test_entry_can_be_found(self):
        self.assertTrue(self.diary.is_locked)
        self.diary.unlock_diary('password')
        self.diary.create_entry("title", "body")
        self.diary.create_entry("title", "body")
        found = self.diary.find_entry(2)
        self.assertEqual(found, self.diary.find_entry(2))

    def test_that_find_entry_entry_not_found_throws_exception(self):
        self.assertTrue(self.diary.is_locked)
        self.diary.unlock_diary('password')
        self.diary.create_entry("title", "body")
        with self.assertRaises(EntryNotFoundException):
            self.diary.find_entry(2)

    def test_that_incorrect_password_throws_exception(self):
        self.assertTrue(self.diary.is_locked)
        with self.assertRaises(IncorrectPasswordException):
            self.diary.unlock_diary("1234")
