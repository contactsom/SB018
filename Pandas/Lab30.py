
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

# Print the result
print(df.to_string())




