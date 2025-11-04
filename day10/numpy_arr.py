import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6])
print("1-D array:\n", arr1)
print("Shape:", arr1.shape)
print("Dimension:", arr1.ndim)
print("Data Type:", arr1.dtype, "\n")

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2-D array:\n", arr2)
print("Shape:", arr2.shape)
print("Dimension:", arr2.ndim)
print("Data Type:", arr2.dtype, "\n")

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3-D array:\n", arr3)
print("Shape:", arr3.shape)
print("Dimension:", arr3.ndim)
print("Data Type:", arr3.dtype, "\n")

arr4 = np.reshape(arr1, (2, 3))
print(arr4, "\n")

arr5 = np.reshape(arr2, (1, 2, 3))
print(arr5, "\n")

arr6 = np.reshape(arr2, (3, 2))
print(arr6, "\n")