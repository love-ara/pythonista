def returns_largest_element(numbers):
	max_element = 0
	for element in numbers:
		if element > max_element:
			max_element = element
	return max_element
		
#print(returns_largest_element([2, 5, 8, 7]))