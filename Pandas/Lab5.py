
'''
What is a Series?
A Pandas Series is like a column in a table.
It is a one-dimensional array holding data of any type.
'''
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print(myvar[0])
