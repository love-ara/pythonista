
def lst_of_numbers(numbers):
    return list(range(1, numbers + 1))

def duplicate_elements(numbers):
    duplicated_lst = []
    for number in numbers:
        duplicated_lst.append(number)
        duplicated_lst.append(number)
    return duplicated_lst


def remove_duplicates(numbers):
    return list(set(numbers))


def add_every_third_element(numbers):
    total = 0
    for item in range(2, len(numbers), 3):
        total += numbers[item]
    return total


def add_first_middle_and_last(numbers):
    if len(numbers) < 3:
        return "the list should contain at least 3 elements"
    else:
        middle = len(numbers) // 2
    if len(numbers) % 2 == 0:
        middle = numbers[middle - 1] + numbers[middle]
    else:
        middle = numbers[middle]
    return numbers[0] + middle + numbers[-1]


def store_in_collection(numbers):
    numbers_set = set()
    for number in numbers:
        numbers_set.add(number)
        if len(numbers_set) == 10:
            break
    return numbers_set

def sum_collection(numbers_set):
    return sum(numbers_set)


def remove_item(numbers, number):
    if number in numbers:
        numbers.remove(number)
        return number
    else:
        return None

def find_intersection(numbers_set1, numbers_set2):
    return numbers_set1.intersection(numbers_set2)

