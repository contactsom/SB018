
'''
Duplicate rows are rows that have been registered more than one time.

'''

import pandas as pd

# Read the data correctly by treating whitespace as delimiter
df = pd.read_csv('mydata1.csv', sep='\s+')

# Remove any extra whitespace in column names
df.columns = df.columns.str.strip()

# Remove single quotes from the 'Date' column
df['Date'] = df['Date'].astype(str).str.replace("'", "", regex=False)

# Convert to datetime safely, allowing mixed formats
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.dropna(subset=['Date'], inplace = True)

'''
 value should be "45" instead of "450", 
 and we could just insert "45" in row 7:
'''
df.loc[7, 'Duration'] = 45

'''
Loop through all values in the "Duration" column.
If the value is higher than 120, set it to 120:
'''
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120


#Returns True for every row that is a duplicate, otherwise False:

print("IS Duplicate :: ",df.duplicated())
df.drop_duplicates(inplace = True)

# Print the result
print(df.to_string())




