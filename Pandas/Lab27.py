
'''
If you want to change the original DataFrame, use the inplace = True argument:
'''

import pandas as pd

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())



