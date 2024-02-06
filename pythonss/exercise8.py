score = float(input("Enter a score ")
total = 0
count = 0
while score != -1:
	total += score
	count += 1
	score = float(input("Enter scores"))

average = total / count
print("The average score is ", average)