from python import list_exercise1


class TestListExercise1:

    def test_list_function_returns_length_of_list(self):
        sample_list = list(range(10, 20))
        assert 10 == list_exercise1.get_length(sample_list)
        assert 26 == list_exercise1.get_length(list(range(10, 25)))


    def test_that_function_returns_sum_of_even_numbers(self):
        sample_list = list(range(10, 20))
        assert 10 == list_exercise1.get_sum_of_even()
