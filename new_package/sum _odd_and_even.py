

sum_of_odd_numbers = 0
sum_of_even_numbers = 0
number = int(input("Enter a number: "))
for i in range(number):
    if i % 2 == 0:
        sum_of_even_numbers += i
    elif i % 2 == 1:
        sum_of_odd_numbers += i

print(f'sum even number {sum_of_even_numbers}')
print(f'sum of odd number {sum_of_odd_numbers}')

try:
    number = int(input("Enter a number: "))
    sum_of_odd_numbers = sum(list(range(1, number)[::2]))
    sum_of_even_numbers = sum(list(range(1, number)[1::2]))
    print(f'sum of even number {sum_of_even_numbers}')
    print(f'sum of odd numbers {sum_of_odd_numbers}')
except ValueError:
    print('Invalid')


number = int(input("Enter a number: "))
print(sum(filter(lambda x: x % 2 == 0, range(1, number))))
print(sum(filter(lambda x: x % 2 != 0, range(1, number))))


def sum_odd_and_even2(number):
    even_sum = 0
    odd_sum = 0
    for i in range(number):
        if i % 2 == 0: even_sum += i
        else: odd_sum += i
    return even_sum, odd_sum

print(sum_odd_and_even2(6))