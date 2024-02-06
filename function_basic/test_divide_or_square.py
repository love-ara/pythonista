import divide_or_square

def test_divider():
	assert divide_or_square.divider(25) == f"{5.0} is the square root of {25}"
	assert divide_or_square.divider(21) == f"{1} \n{21} is not divisible by 5"
