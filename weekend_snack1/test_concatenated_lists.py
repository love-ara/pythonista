import concatenated_lists

def test_concatenator():
	assert concatenated_lists.concatenator(['a', 'b', 'c'], [1, 2, 3]) == ['a', 'b', 'c', 1, 2, 3]