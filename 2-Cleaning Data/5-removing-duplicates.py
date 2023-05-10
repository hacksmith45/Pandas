# Discovering Duplicates
# Duplicate rows are rows that have been registered more than one time.


# By taking a look at our test data set, we can assume that row 11 and 12 are duplicates.

# To discover duplicates, we can use the duplicated() method.

# The duplicated() method returns a Boolean values for each row:

# print(df.duplicated()) 

# Returns True for every row that is a duplicate, othwerwise False:

import pandas as pd

df = pd.read_csv('C:/Users/HP/Desktop/Pandas/2-Cleaning Data/data.csv')

df.drop_duplicates(inplace = True)

print(df.to_string())


# Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, 
# but it will remove all duplicates from the original DataFrame.