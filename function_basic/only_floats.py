def floating_nums(num1, num2):
	if type(num1) == float and type(num2) == float:
		return 2
	elif type(num1) == float or type(num2) == float:
		return 1
	
	else:
		return 0

#print( floating_nums(1.1, 1.1))
#print( floating_nums(12, 12.1))
#print( floating_nums(12.1, 10))
#print(floating_nums(1, 1))
#print(floating_nums('ayo', 'ara'))
