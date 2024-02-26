import unittest

from package.diary import Diary


class TestDiary(unittest.TestCase):
    def setUp(self):
        self.diary = Diary('username', 'password')

    def test_diary_is_locked(self):
        self.assertTrue(self.diary.is_locked())

    def test_diary_is_be_unlocked(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary('password')
        self.assertFalse(self.diary.is_locked())

    def test_entry_can_be_created(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary('password')
        self.diary.create_entry('title', 'body')
        self.assertEqual(1, len(self.diary.entries))

    def test_entry_can_be_deleted(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary('password')
        self.diary.create_entry('title', 'body')
        self.diary.create_entry('new_title', 'body')

        self.assertEqual(2, self.diary.get_number_of_entry())

        self.diary.delete_entry(2)

        self.assertEqual(1, self.diary.get_number_of_entry())

