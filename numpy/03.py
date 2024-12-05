#3 : Using arange() function

import numpy as np 

arr = np.arange(15, dtype=np.int64)

print(arr)  #[0 4 8 12 16]
print(type(arr))
print(arr.dtype)
print(arr.itemsize)