def divider(number):
	if number%5 == 0:
		return f"{number**0.5} is the square root of {number}"
	elif number%5 != 0:
		return f"{number%5} \n{number} is not divisible by 5"
		
 
#print(divider(25))
#print(divider(21))