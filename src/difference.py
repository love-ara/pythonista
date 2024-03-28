def difference(numbers):
    maxi = numbers[0]
    mini = numbers[0]
    for number in numbers:
        if number > maxi:
            maxi = number
        if number < mini:
            mini = number
    return [maxi - mini]
