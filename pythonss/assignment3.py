n = float(input("Enter all numbers (press zero to get result): "))
total = 0
counter = 0
while n != 0:
	total += n
	counter += 1
	n = float(input("Enter all numbers: "))

average = total / counter
sum = total
print("sum =", sum)
print("average = ", average)

