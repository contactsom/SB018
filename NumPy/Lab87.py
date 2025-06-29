'''
NumPy String capitalize() Function
'''

import numpy as np

array1 = np.array(['nEpalI', 'AmeriCAN', 'CaNadIan'])

# convert all string elements to uppercase
result1 = np.char.upper(array1)

# convert all string elements to lowercase
result2 = np.char.lower(array1)

print("To Uppercase: ",result1)
print("To Lowercase: ",result2)