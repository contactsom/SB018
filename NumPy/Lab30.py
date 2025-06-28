'''
Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character,
like i for integers, u for unsigned integers etc.
Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''

import numpy as np

#arr = np.array([1.1, 2.1, 3.1])
arr = np.array(['a', '2', '3'], dtype='i')

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

