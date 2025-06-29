'''
numpy.join() : This function is a string method and returns a string
in which the elements of sequence have been joined by str separator.
'''

import numpy as np

# splitting a string
print(np.char.join('-', 'geeks'))

# splitting a string
print(np.char.join(['-', ':'], ['geeks', 'for']))