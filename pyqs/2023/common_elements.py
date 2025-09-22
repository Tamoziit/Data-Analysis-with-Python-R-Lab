x = [1, 2, 3, 4, 5]
y = [3, 4, 5, 6, 7]

z1 = [item for item in x if item in y]
z2 = list(filter(lambda item: item in x, y))

print(z1)
print(z2)