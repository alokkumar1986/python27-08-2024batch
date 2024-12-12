import numpy as np

# arr = np.arange(24).reshape(4,6)
# arr = np.arange(24).reshape(2, 12)
arr = np.arange(24).reshape(3, 8)
# print(arr)
'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
'''

newarr = np.hsplit(arr, 2)
'''
array([[0, 1, 2, 3, 4, 5], [12, 13, 14, 15, 16, 17]]),
array([[6,7,8, 9, 10, 11], [18, 19, 20, 21, 22, 23]])
'''
print(newarr)

