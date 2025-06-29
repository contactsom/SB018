'''
numpy.split() : This function returns a list of strings after breaking the
given string by the specified separator.
'''

import numpy as np

# splitting a string
print(np.char.split('geeks for geeks'))

# splitting a string
print(np.char.split('geeks, for, geeks', sep=','))