

def even_position_checker(numbers):
	count = len(numbers)
	even_positions = numbers[1: count : 2]
	return even_positions

print(even_position_checker([1, 2, 3, 4, 5, 6, 7, 8, 9]))