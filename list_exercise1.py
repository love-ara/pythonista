




# def __get_length():
#     count = 0
#     for i in numbers:
#         count+=1
#     return count



def get_sum_of_even(numbers):
    return sum(numbers [1: : 2])


def get_sum_of_odd(numbers):
    return sum(numbers[::2])


def get_product(numbers):
    product = 1
    for index in range(2, len(numbers), 3):
        product *= numbers[index]
    return product
