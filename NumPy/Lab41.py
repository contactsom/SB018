'''
Reshaping arrays
Reshaping means changing the shape of an array.
The shape of an array is the number of elements in each dimension.
By reshaping we can add or remove dimensions or change number of elements in each dimension.
'''

'''
Iterating Arrays
Iterating means going through elements one by one.
As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
If we iterate on a 1-D array it will go through each element one by one.
'''
import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)