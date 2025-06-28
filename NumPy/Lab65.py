'''
Searching Arrays
You can search an array for a certain value, and return the indexes that get a match.
To search an array, use the where() method.
'''

'''
Find the indexes where the values are odd:
'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)