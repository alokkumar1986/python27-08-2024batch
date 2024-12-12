import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3,3)
#print(arr1) [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr2 = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
#print(arr2) [[1, 2, 3], [4, 5, 6]]
arr3 = np.array([1, 2, 3, 4, 5, 6]).reshape(3, 2)
arr4 = np.array([1, 2, 3]).reshape(3, 1)

# arr5 = np.vstack((arr1, arr2)) #[[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6]]

# print(arr5)

# arr6 = np.hstack((arr1, arr1)) 

# print(arr6)

arr5 = np.concatenate((arr1, arr2), axis=0) #[[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6]]

print(arr5)

hstack
# arr1 = 3X3
# arr2 = 3Xx
vstack
# arr1 = 1X3
# arr2 = xX3

