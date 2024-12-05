#2 : creating array using fromiter()

import numpy as np 

s = { 1 : 'Aptech', 2 : 'numpy', 4: 5    }

arr = np.fromiter(s, dtype = np.int64)

print(arr)
print(type(arr))
print(arr.dtype)
print(arr.itemsize)