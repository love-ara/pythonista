language = input("Enter your prefered language: ")

match language: 
	case 'java':
		print("A Java Pro")
	case 'python':
		print('pythonista')
	case _:
		print('this is the default')