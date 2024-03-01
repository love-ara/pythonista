
digits = list(range(1, 51))

print(list(filter(lambda number: number % 2 == 0, digits)))
print(list(map(lambda number: number ** 2, digits)))