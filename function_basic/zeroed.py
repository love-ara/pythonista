def zeroer(numbers):
	if len(numbers) > 1:
		numbers[0] = 0
		numbers[-1] = 0
		return numbers

#print(zeroer([2, 5, 8, 7, 9]))