import unittest

from src.letters_and_digits import countLettersAndDigits, count_upperCaseLetters


class TestLettersAndDigits(unittest.TestCase):
    def test_function_can_count_letters_and_digits(self):
        self.assertEqual("LETTER 10 DIGIT 3", countLettersAndDigits("hello world! 123"))

    def test_function_can_count_uppercase_letters(self):
        self.assertEqual("UPPERCASE 1 LOWER CASE 9 ", count_upperCaseLetters("Hello world! 123"))
