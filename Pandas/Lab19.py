
'''
You can change the maximum rows number with the same statement.
'''

import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df)




