# import pytest
import List_exercise


def test_that_numbers_list_are_stored():
    assert List_exercise.store_in_a_list() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_get_length_of_the_lst():
    assert List_exercise.get_length_of_the_lst() == 10


def test_sum_elements_at_even_positions():
    assert List_exercise.sum_elements_at_even_positions() == 30


def test_sum_elements_at_odd_positions():
    assert List_exercise.sum_elements_at_odd_positions() == 25


def test_multiply_elements_at_third_positions():
    assert List_exercise.multiply_elements_at_third_positions() == 945


def test_average_of_elements_the_list():
    assert List_exercise.average_of_elements_the_list() == 5.5


def test_get_largest_elements_of_the_list():
    assert List_exercise.get_largest_elements_of_the_list() == 10


def test_get_smallest_elements_of_the_list():
    assert List_exercise.get_smallest_elements_of_the_list() == 1


def test_get_strings_from_the_list():
    assert List_exercise.get_strings_from_the_list(['apple', 'aramida', 'apple', 'anna']) == ['aramida', 'anna']
