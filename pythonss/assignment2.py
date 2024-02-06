age = int(input("Input a dog\'s age in human years: "))

if age <= 2:
	dog_age = age * 10.5

if age > 2:
	dog_age = (10.5 * 2) + (age - 2)*4
print("the dog\'s age in dog\'s year is", dog_age)	