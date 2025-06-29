
'''
Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead.
This way you do not have to delete entire rows just because of some empty cells.
The fillna() method allows us to replace empty cells with a value:
'''

import pandas as pd

df = pd.read_csv('mydata.csv')

df.dropna(inplace = True)

print(df.to_string())



