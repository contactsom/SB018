
'''
Replace Only For Specified Columns
The example above replaces all empty cells in the whole Data Frame.
To only replace empty values for one column, specify the column name for the DataFrame:
'''

import pandas as pd

df = pd.read_csv('mydata.csv')
df.fillna({"Calories": 130}, inplace=True)
print(df.to_string())



