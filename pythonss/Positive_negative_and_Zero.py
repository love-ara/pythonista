num = int(input("Enter any number and -1 to end: "))

positives = 0
negatives = 1
zeros = 0
count = 0

while num != -1:
	if num > 0:
		positives += 1
		count += 1

	if num < 0:
		negatives += 1
		count += 1

	if num == 0:
		zeros += 1
		count += 1
	num = int(input("Enter a number: "))

print("Positive numbers are ", positives)
print("Negative numbers are ", negatives)
print("The zeros are ",  zeros)