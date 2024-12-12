#   copy()
#   view()
import numpy as np
'''
arr = np.array([1, 2, 3, 4, 5])

arr1 = arr.view()

print(arr)
print(arr1)

arr[3] = 44

print(arr)
print(arr1)

arr1[3] = 55

print(arr)
print(arr1)
'''
arr = np.array([1, 2, 3, 4, 5])

arr1 = arr.copy()

print(arr)
print(arr1)

arr[3] = 44

print(arr)
print(arr1)

arr1[3] = 55

print(arr)
print(arr1)





