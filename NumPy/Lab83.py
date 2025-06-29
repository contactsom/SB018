'''
String Comparison
numpy.greater(): This function checks whether string1 is greater than string2 or not.
'''

import numpy as np

# comparing a string elementwise
a = np.char.greater('geeks', 'for')

print(a)