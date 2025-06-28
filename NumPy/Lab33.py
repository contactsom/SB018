'''
The Difference Between Copy and View
The main difference between a copy and a view of an array is that the copy is a new array,
and the view is just a view of the original array.
'''

#Make a copy, change the original array, and display both arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)