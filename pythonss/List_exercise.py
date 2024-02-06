

def store_in_a_list():
    the_lst = []
    for numbers in range(1, 11):
        the_lst.append(numbers)
    return the_lst


def  get_length_of_the_lst():
    count = 0
    for numbers in store_in_a_list():
        count+=1
    return count



def  sum_elements_at_even_positions():
    sum_of_even = 0
    for index in range(1, get_length_of_the_lst(), 2 ):
        sum_of_even += store_in_a_list()[index]
    return sum_of_even



def sum_elements_at_odd_positions():
    sum_of_odd = 0
    for index in range(0, get_length_of_the_lst(), 2 ):
        sum_of_odd += store_in_a_list()[index]
    return sum_of_odd




def multiply_elements_at_third_positions():
    multiplied_elements = 1
    for index in range(0, get_length_of_the_lst(), 2):
        multiplied_elements *= store_in_a_list()[index]
    return multiplied_elements

def average_of_elements_the_list():
    average = 0
    for index in range(0, get_length_of_the_lst()):
        average += store_in_a_list()[index]/get_length_of_the_lst()
    return average

def get_largest_elements_of_the_list():
    largest_elements = store_in_a_list()[0]
    for element in store_in_a_list():
        if element > largest_elements:
            largest_elements = element
    return largest_elements

def get_smallest_elements_of_the_list():
    lowest_elements = store_in_a_list()[0]
    for element in store_in_a_list():
        if element < lowest_elements:
            lowest_elements = element
    return lowest_elements



def get_strings_from_the_list(words):
    lst = []
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            lst.append(word)
    return lst


print(get_strings_from_the_list(['apple', 'aramida', 'apple', 'anna']))
print(store_in_a_list())
print(get_length_of_the_lst())
print(sum_elements_at_even_positions())
print(sum_elements_at_odd_positions())
print(multiply_elements_at_third_positions())
print(average_of_elements_the_list())
print(get_largest_elements_of_the_list())
print(get_smallest_elements_of_the_list())




