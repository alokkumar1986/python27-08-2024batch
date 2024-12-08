import numpy as x 

arr = x.arange(10)

arr2d = arr.reshape(5, 2)

print(arr)
print(arr2d)

print(arr.ndim)
print(arr2d.ndim)

print(arr2d[2, 1]) #5