
def reverser(numbers):
	for element in numbers:
	#reverse_numbers = numbers[::-1]
	#reverse_numbers = [ item for item in reversed(numbers)]
		reverse_numbers = [element for element in reversed(numbers)]
	return reverse_numbers
	
print(reverser([2, 5, 8, 7, 9]))