import numpy as np

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

elements = []
print(f"Enter {r * c} integer elements:")
for i in range(r * c):
    elements.append(int(input(f"Element {i+1}: ")))

mat = np.array(elements).reshape(r, c)
print(mat, "\n")
n = np.sort(mat, axis = 1) # sorting row
p = np.sort(mat, axis  = 0) # sorting col
print(n, "\n")
print(p, "\n")

data = p.flatten()
print("Min:", np.min(data))
print("Max:", np.max(data))
print("Range:", np.ptp(data))
print("70th percentile:", np.percentile(data, 70))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Variance:", np.var(data))
print("STandard Deviation:", np.std(data))