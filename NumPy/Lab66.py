'''
Search Sorted
There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
The searchsorted() method is assumed to be used on sorted arrays.
'''

'''
Find the indexes where the value 7 should be inserted:
'''
import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)