
total = 0
count = 1
while count <= 20:
	number = int(input(f"Enter number {count} : "))
	total += number
	count += 1
print('The sum equals', total)



total = 0
for items in range(20):
	number = float(input("Enter number: "))
	total += number
print(total)