#def student_fullname(first_name, last_name):
	#"""this function takes 2 args. first name and last name. 
	#displays the fullnmae"""
	#student_fullname = str(input(""))
	#return f"{first_name} {last_name}"

#print(student_fullname("dayo", "akinyemi"))
#print(student_fullname("" , ""))
#print(help(print))


#def add_stuff(n, m):
#def add_stuff(n, m=5)
	#return n + m

#print(add_stuff(2, 3))
#print(add_stuff(4,6))
#print(add_stuff('franklin' , 'sussannah'))

def maximum_num(m, n, o):
		largest = 0
		if m > n and m > o:
			largest = m
		elif n > m and n > o:
			largest = n
		else :
			largest = o
		return f"{largest} is the largest number"

print(maximum_num(2, 5, 7))
print(maximum_num(6, 5, 2))

#def largest(number1, number2, number3):
	#if number1 > number2 and number1 > number3:
		#return number1
	#elif number2 > number1 and number2 > number3:
		#return number2
	#else: 
		#return number3
#print(largest(3, 8, 9))