import check_for_palindrome

def  test_palindrome_checker():
	assert check_for_palindrome.palindrome_checker(['a', 'r', 'a'] ) == True
	assert check_for_palindrome.palindrome_checker(['a', 'y', 'o'] ) == False