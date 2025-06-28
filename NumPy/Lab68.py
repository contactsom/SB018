'''
Multiple Values
To search for more than one value, use an array with the specified values.
'''

import numpy as np

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)