'''
String Comparison
numpy.not_equal(): This function checks whether two string is unequal or not.
'''

import numpy as np

# Comparing a string element-wise using not_equal() method
a = np.char.not_equal('geeks', 'for')

print(a)