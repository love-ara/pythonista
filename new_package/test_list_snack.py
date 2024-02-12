import unittest
from new_package import list_snack

class TestListSnack(unittest.TestCase):


    def test_function_can_store_numbers_in_a_list(self):
        numbers = 10
        expected = list(range(1, numbers + 1))
        self.assertEqual(expected, list_snack.lst_of_numbers(numbers))

    def test_list_can_duplicate(self):
        numbers = [1, 2, 3, 4, 5]
        expected_result = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        self.assertEqual(expected_result, list_snack.duplicate_elements(numbers))


    def test_list_can_remove_duplicates(self):
        number = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(expected_result, list_snack.remove_duplicates(number))


    def test_list_can_add_every_third_element(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_result = 18
        self.assertEqual(expected_result, list_snack.add_every_third_element(numbers))

    def test_that_list_can_add_first_middle_and_last_elements(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_result = 15
        self.assertEqual(expected_result, list_snack.add_first_middle_and_last(numbers))


    def test_that_function_store_in_collection_without_duplicates(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_result = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        self.assertEqual(expected_result, list_snack.store_in_collection(numbers))


    def test_that_function_sum_collection(self):
        numbers = {1, 2, 3, 4, 5, 6, 7, 8}
        expected_result = 36
        self.assertEqual(expected_result, list_snack.sum_collection(numbers))

    def test_that_function_can_remove_an_item(self):
        numbers = [1, 2, 3, 4, 5, 6, 7]
        number = 3
        expected_result = 3
        self.assertEqual(expected_result, list_snack.remove_item(numbers, number))

    def test_find_intersection(self):
        set1 = {1, 2, 3, 4}
        set2 = {3, 6, 7, 4}
        expected_intersection = {3, 4}
        self.assertEqual(expected_intersection, list_snack.find_intersection(set1, set2))

