odd_numbers = 0
even_numbers = 0

for number in range(1, 101):
	if number%2 == 0:
		even_numbers += 1
	if number%2 !=0: 
		odd_numbers += 1

print("Number of odd number:", odd_numbers)
print("Number of even number:", even_numbers)
