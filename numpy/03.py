#3 : Using arange() function

import numpy as np 


'''
arr = np.arange(15, dtype=np.int64)

print(arr)  #[0 4 8 12 16]
print(type(arr))
print(arr.dtype)
print(arr.itemsize)
'''

a = np.array([1, 2, 3, 4, 5])

print(a[4])  #5

b = np.array([[1, 2, 3], [4, 5, 6]])

print(b[1, 2]) #6

c = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]] ])

print(c[1, 1, 2])  #12

print(c[0, 1, 2])  #6


arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(arr[0, 1, 1]) # 4