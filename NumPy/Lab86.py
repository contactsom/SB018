'''
NumPy String capitalize() Function
'''

import numpy as np

# define an array with three string elements
array1 = np.array(['eric', 'paul', 'sean'])

# capitalize the first letter of each string in array1
result = np.char.capitalize(array1)

print(result)

# Output: ['Eric' 'Paul' 'Sean']