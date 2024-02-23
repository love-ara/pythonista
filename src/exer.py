from time import time

def decorate(fn):
    def inner(*args, **kwargs):
        print("****************")
        print(fn(*args, **kwargs))
        print("****************")
    return inner

@decorate
def show_name(name):
    return name

show_name("Ara")

def time_taken(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"it  took {t2 - t1:.3f}ms to execute")
        return result
    return wrapper

@time_taken
def get_list(numbers):
    result = []
    for i in range(numbers):
        result.append(i)
    return result


get_list(numbers=100000)

def gun(name, number = 00):
    return f'{name} & {number}'

print(gun("Ara"))