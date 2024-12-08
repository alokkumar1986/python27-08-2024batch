import numpy as np

arr = np.empty([2, 3], dtype=np.int64, order="F")

print(arr)

arr1 = np.ones([2, 3], dtype=np.int64, order="F")
print(arr1)


arr2 = np.zeros([2, 3], dtype=np.int64, order="F")
print(arr2)


arr3 = np.ones([4,5], dtype=np.int64, order="F")

print(arr3)