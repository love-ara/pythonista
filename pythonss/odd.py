odd_numbers = 0
sum = 0
for numbers in range(1000, 5001):
	if numbers%2 != 0:
		odd_numbers += 1
		sum += numbers

print(sum)


sum = 0
count = 1000

while(count <= 5000):

	if count%2 != 0:
		sum += count 
	count += 1

print(sum)
	

odd_numbers = 0
sum = 0
#numbers = 1000
for numbers in range(1000, 5001):
	if numbers%2 != 0:
		odd_numbers += 1
		sum += numbers 
	numbers += 1
	

print(sum)		