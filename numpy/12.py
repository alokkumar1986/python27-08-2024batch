import numpy as np

arr = np.arange(24).reshape(4,6)

# [0,.....5]
# [6,.....11]
# [12,....17]
# [18,....23]


newarr = np.vsplit(arr, 2)

print(newarr)