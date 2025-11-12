import numpy as np
import pandas as pd

#1
arr1 = np.array([1, 2, 3, 4, 5, 6])
print(arr1)
print(arr1.shape)
print(arr1.ndim)
print(arr1.dtype, "\n")

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print(arr2.shape)
print(arr2.ndim)
print(arr2.dtype, "\n")

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3)
print(arr3.shape)
print(arr3.ndim)
print(arr3.dtype, "\n")

arr4 = arr3.reshape(3, 2, 2)
print(arr4, "\n")
arr5 = arr2.reshape(1, 2, 3)
print(arr5, "\n")

#2
zeros = np.zeros(10)
print(zeros, "\n")

ones = np.ones((2,5), dtype=int)
print(ones, "\n")

myarr = np.arange(4, 4 + (3 * 5 *4), 4, dtype=int).reshape(3, 5)
print(myarr, "\n")

base_arr = np.array([1, 2, 3])
tiled_array = np.tile(base_arr, 3)
series_obj = pd.Series(tiled_array)
print(tiled_array, "\n")
print(series_obj, "\n")

#3
ranarr = np.random.rand(2, 3)
print(ranarr, "\n")
onearr = np.ones((2, 3), dtype=int)
print(onearr, "\n")
boolarr = ranarr > 0.5
print(boolarr)
print(boolarr.shape, "\n")
newarr = onearr[boolarr]
print(newarr)
print(newarr.shape, "\n")