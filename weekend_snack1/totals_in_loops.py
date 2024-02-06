
def for_looper(numbers):
	sum = 0
	count = 0
	for elements in numbers:
		sum+=elements
		count = 1
	return sum


def while_looper(numbers):
	count = 0
	total = 0
	while count < len(numbers): 
		total += numbers[count]
		count += 1
	return total


def do_while_looper(numbers):
	sum = 0
	count = 0
	while True:
		count <= len(numbers)
		sum+=count
		if count > len(numbers):
			break
		count+=1
	return sum
		

#print(for_looper([5, 5, 5, 5]))
#print(while_looper([2, 2, 1, 2]))
#print(do_while_looper([3, 2, 5, 5]))