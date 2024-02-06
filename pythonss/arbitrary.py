scores = int(input("Enter a student score but enter -1 to terminate : "))


pass_mark = 0
fail = 0


while scores != -1:

	if scores < -1 or scores > 100:
		print("Not valid")
	elif scores >= 45:
		pass_mark += 1
	elif scores < 45:
		fail += 1
	scores = int(input("Enter a student score : "))

	
print()
print('The number of student that pass: ', pass_mark)

print('The number of student that failed: ', fail)