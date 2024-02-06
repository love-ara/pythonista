import combined_lists

def test_combiner():
	assert combined_lists.combiner(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]