matrix = [
    [4, 5, 6],
    [8, 2, 1],
    [12, 8, 0]
]

res = [
    [x for x in row if x % 4 == 0]
    for row in matrix if sum(row) <= 15
]

print("Original matrix:")
for row in matrix:
    print(row)

print("\nFiltered matrix:")
for row in res:
    print(row)