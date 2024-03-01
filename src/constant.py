import math


def constant():
    numbers = input("Enter D: ")
    numbers = numbers.split(',')

    result_list = []
    result = ''
    for D in numbers:
        Q = round(math.sqrt(2 * 50 * int(D) / 30))
        result_list.append(Q)
        result = ' , '.join(map(str, result_list))
    return result


print(constant())
