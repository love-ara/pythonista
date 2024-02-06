import even_position

def test_even_position_checker():
	assert even_position.even_position_checker([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6, 8]