'''
In NumPy, we use the np.char.add() function
to perform element-wise string concatenation for two arrays of strings
'''

import numpy as np

array1 = np.array(['iPhone: ', 'price: '])
array2 = np.array(['15', '$900'])

# perform element-wise array string concatenation
result = np.char.add(array1, array2)

print(result)