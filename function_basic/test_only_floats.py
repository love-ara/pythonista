import only_floats

def test_floating_nums():
	assert only_floats.floating_nums(12.3, 10.1) == 2
	assert only_floats.floating_nums(12.3, 10) == 1
	assert only_floats.floating_nums(10, 10.1) == 1
	assert only_floats.floating_nums(12, 90) == 0