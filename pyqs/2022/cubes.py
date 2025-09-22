x = [1, 2, 3, 4, 5]

y = list(map(lambda item: item ** 3, filter(lambda item: item % 2 != 0, x)))

print(y)