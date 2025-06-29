'''
numpy.count() : This function returns the number of occurrences
 of a substring in the given string.
'''

import numpy as np

a = np.array(['geeks', 'for', 'geeks'])

# counting a substring
print(np.char.count(a, 'geek'))

# counting a substring
print(np.char.count(a, 'fo'))