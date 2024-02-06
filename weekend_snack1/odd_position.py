
def odd_position_checker(numbers):
	#for elements in numbers:
	odd_positions = numbers[0:len(numbers):2]
	return odd_positions

print(odd_position_checker([1, 2, 3, 4, 5]))
