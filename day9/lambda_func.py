a = [x for x in range(0, 20)]
print("Original List:", a)

g = filter(lambda x: x % 2 == 0 and x % 3 == 0, a)
lst1 = list(g)
print("Nos. divisible by 2 & 3:", lst1)

sq = map(lambda x: x * x, a)
c = map(lambda x: x * x * x, a)
lst2 = list(sq)
lst3 = list(c)

print("Squares:", lst2)
print("Cubes:", lst3)