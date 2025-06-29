
'''
Data Cleaning
Data cleaning means fixing bad data in your data set.
Bad data could be:
Empty cells
Data in wrong format
Wrong data
Duplicates
In this tutorial you will learn how to deal with all of them.

The data set contains some empty cells ("Date" in row 22, and "Calories" in row 18 and 28).

The data set contains wrong format ("Date" in row 26).

The data set contains wrong data ("Duration" in row 7).

The data set contains duplicates (row 11 and 12).


Remove Rows
One way to deal with empty cells is to remove rows that contain empty cells.
This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
'''

import pandas as pd

df = pd.read_csv('mydata.csv')
new_df = df.dropna()
print(new_df.to_string())




