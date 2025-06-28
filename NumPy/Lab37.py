'''
Get the Shape of an Array
NumPy arrays have an attribute called shape that returns a tuple with each index having the
number of corresponding elements.
'''

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)