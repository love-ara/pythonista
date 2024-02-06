number = int(input("Enter your 5-digits number "))
 
first_digit = number%10
first_number = number/10
second_digit = first_number%10
second_number = first_number/10
third_digit = second_number%10
third_number = second_number/10
fourth_digit = third_number%10
fourth_number = third_number/10
fifth_digit = fourth_number%10
fifth_number = fourth_number/10
print(first_number, second_number, third_number, fourth_number, fifth_number)