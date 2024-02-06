number1 = int(input("Enter an integer "))
number2 = int(input("Enter another integer "))
number3 = int(input("Enter one last integer:"))

sum = number1 + number2 + number3
average = (number1 + number2 + number3)/3
product = number1 * number2 * number3
print('sum =', sum)
print('average =', average)
print('product =', product)


min = number1
if number2 < min :
		min = number2
if number3 < min :
	min = number3
print(min, "is the smallest number")
 
max = number1
if number2 > max:
	max = number2
if number3 > max:
        max = number3
print(max, " is the largest number")

