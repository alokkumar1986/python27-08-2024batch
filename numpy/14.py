import numpy as np

arr = np.arange(23)

print(arr) #[0, 1, 2, 3, 4................22]

arr1 = np.where(arr%3==0) #numpy search

print(arr1) #array(([0,3, 6, 9, 12, 15, 18, 21]),)