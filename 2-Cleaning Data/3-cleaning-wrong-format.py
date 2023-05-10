# Data of Wrong Format
# Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

# To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.


# Convert Into a Correct Format
# In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, 
# the 'Date' column should be a string that represents a date:


# Let's try to convert all cells in the 'Date' column into dates.

# Pandas has a to_datetime() method for this:

import pandas as pd

df = pd.read_csv('C:/Users/HP/Desktop/Pandas/2-Cleaning Data/data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())


# Removing Rows
# The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, 
# and we can remove the row by using the dropna() method.

df.dropna(subset=['Date'], inplace = True)