#ways to create numpy array
#1: Using array() function
import numpy as np 
lst = [1, 2, 3, 4, 5]
# arr = np.array([1, 2, 3, 4, 5])
arr = np.array(lst, dtype=np.int32)
print(type(arr))  # object of ndarray
print(arr.dtype)  # data type of the values
print(arr.itemsize) # bytes of datatype 
print(arr)
# print(lst)
print(arr[1])