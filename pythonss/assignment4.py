prime_number = 1
for items in range(1, 100):
	while prime_number >= 1:
		if prime_number / 2 and prime_number%2 != 0:
			prime_number = 1
			print(items)


