#numpy operations

import numpy as np
'''
arr = np.array([[1,2,3,4], [5, 6, 7, 8]])
arr1 = arr+1  #Vectorised operation
print(arr1)

'''
arr = np.array([[1, 2, 3, 4], [5, 6, 7,8]])
arr1 = np.array([6, 7, 8, 9])
arr2 = np.add(arr, arr1)
print(arr2)
arr3 = np.subtract(arr, arr1)
print(arr3)
arr4 = np.multiply(arr, arr1)
print(arr4)

arr5 = np.divide(arr, arr1)
print(arr5)

arr6 = np.mod(arr, arr1)
print(arr6)

arr7 = np.remainder(arr, arr1)
print(arr7)
