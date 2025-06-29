
'''
Calculate the MEAN, and replace any empty values with it:
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


# Print the result
print(df.to_string())




