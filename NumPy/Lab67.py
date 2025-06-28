'''
Search From the Right Side
By default the left most index is returned, but we can give side='right' to return the right most index instead.
'''

import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)