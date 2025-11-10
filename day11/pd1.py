import pandas as pd

arr = pd.Series([0, 1, 2, 3])
print(arr, "\n")

arr.index = ['d', 'b', 'a', 'c']
print(arr, "\n")

print(arr[['b', 'c']])
print(arr[['d', 'a', 'c']])