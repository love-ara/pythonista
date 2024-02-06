
def palindrome_checker(words):
	for letter in words:
		reversed_word = [letter for letter in reversed(words)]
	if reversed_word == words:
		return True
	if reversed_word != words:
		return False
		
	#return reversed_word

#print(palindrome_checker(['a', 'r', 'a', 'm', 'i', 'd', 'e']))
	