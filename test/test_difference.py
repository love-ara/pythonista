import unittest

from src.difference import difference


class Difference(unittest.TestCase):
    def test_difference(self):
        expected = [6]
        actual = [4, 2, 5, 7, 8]
        self.assertEqual(expected, difference(actual))

