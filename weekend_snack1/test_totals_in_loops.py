import totals_in_loops

def test_for_looper():
	assert totals_in_loops.for_looper([5, 5, 5, 5]) == 20



def test_while_looper():
	assert totals_in_loops.while_looper([2, 2, 1, 2]) == 7



def test_do_while_looper():
	assert totals_in_loops.do_while_looper([3, 2, 5, 5]) == 15
