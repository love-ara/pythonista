number = int(input("Enter a number of unit used "))

if number <= 100:
	print("Your charge is N0.0")

if number > 100 and number < 200:
	diff = (number - 100) * 10
	print("Your charge is", diff)

if number >= 200:
	diff1 = (number - 200) * 20 + (100) * 10
	
	print("Your charge is " , diff1)