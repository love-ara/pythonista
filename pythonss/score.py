number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
number3 = int(input("Enter the last number: "))

max = number1
if number2 > max:
	max = number2
if number3 > max:
        max = number3
print(max, " is the highest number")
