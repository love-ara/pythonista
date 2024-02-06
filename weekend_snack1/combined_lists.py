
def combiner(letters, numbers):
	combined_list = []
	combined = min(len(letters), len(numbers))
	
	for items in range(combined):
		combined_list.append(letters[items])
		combined_list.append(numbers[items])


	combined_list.extend(letters[combined:] + numbers[combined:])

	
	return combined_list

#print(combiner(['a', 'b', 'c'], [1, 2, 3]))