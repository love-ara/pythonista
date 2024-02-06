
def number_to_list(numbers):
	new_list = list((int(index)) for index in str(numbers))
	#new_list = [int(number) for number in str(numbers)]
	return new_list

#print(number_to_list(2345))	