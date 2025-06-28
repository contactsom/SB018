'''
Creating the Filter Array

In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.

'''

import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)