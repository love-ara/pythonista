import unittest
from new_package import exercise10
class TestExercise10(unittest.TestCase):

    def test_swap_char(self):
        str1 = 'abc'
        str2 = 'xyz'
        expected = 'xyc abz'
        self.assertEqual(expected, exercise10 .swap_char(str1, str2))
