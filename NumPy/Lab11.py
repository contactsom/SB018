import numpy as np

#Create an array with 5 dimensions and verify that it has 5 dimensions:

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)