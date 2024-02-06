
def totaler(numbers):
	total = 0
	count = 0
	for element in numbers:
		total+= element 
		count += 1
	return total

print(totaler([1, 2, 3, 4]))