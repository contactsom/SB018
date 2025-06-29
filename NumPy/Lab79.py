'''
numpy.rfind() : This function returns the highest index of the substring if found in given string.
If not found then it returns -1.
'''

import numpy as np

a = np.array(['geeks', 'for', 'geeks'])

# counting a substring
print(np.char.rfind(a, 'geek'))

# counting a substring
print(np.char.rfind(a, 'fo'))