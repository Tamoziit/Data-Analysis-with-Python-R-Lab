lst = list(map(int, (x for x in range(0, 10))))
print("List:", lst)

# -------- Mean --------
total = 0
count = 0
for i in lst:
    total += i
    count += 1

mean = total / count

# -------- Median --------
lst.sort()

if count % 2 == 1:  # odd length
    median = lst[count // 2]
else:  # even length
    mid1 = lst[count // 2 - 1]
    mid2 = lst[count // 2]
    median = (mid1 + mid2) / 2

print("Mean =", mean)
print("Median =", median)
