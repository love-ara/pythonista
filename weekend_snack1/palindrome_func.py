def palindrome(word):
	return word == word[::-1]
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 1]
print(palindrome("ana"))
print(palindrome("ara"))
print(palindrome(list1))
print(palindrome(list2))