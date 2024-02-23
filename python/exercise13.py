count = 0
for items in range(1, 10):
	count += 1
	result = (str(count )* items)
	print(result)
			


for items in range(1, 10):
	print(str(items) * items)




for items in range(1, 10):
	count += 1
	print(items * count)


total = 0
for i in range(5):
	score = float(input('Enter score: '))
	total += score
average = total / 5
print(average)	


score = float(input('Enter score: '))
count = 0
while score != -1:
	count += 1
	total += score
	score = float(input('Enter score: '))

print(total / count)