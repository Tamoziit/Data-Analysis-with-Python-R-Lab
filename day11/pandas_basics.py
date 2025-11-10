import pandas as pd
import numpy as np

arr = pd.Series([10, 20, 30, 40])
print(arr)

max = arr.max()
min = arr.min()

print("Max:", max)
print("Min:", min)
print("Sum:", arr.sum())

for i in range(len(arr)):
    if arr[i] == max:
        arr[i] = min
    elif arr[i] == min:
        arr[i] = max
    else:
        continue
    
print(arr)

print("Mean =", arr.mean())
print("Median =", arr.median())

print("Using Numpy:")
print("Mean =", np.mean(arr))
print("Median =", np.median(arr))