# Pandas is a Python library used for working with data sets.

# It has functions for analyzing, cleaning, exploring, and manipulating data.

# The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes 
# McKinney in 2008.


# Why Use Pandas?

# Pandas allows us to analyze big data and make conclusions based on statistical theories.

# Pandas can clean messy data sets, and make them readable and relevant.

# Relevant data is very important in data science.


# Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving 
# information from it.


# What Can Pandas Do?

""" 
Pandas gives you answers about the data. Like:

Is there a correlation between two or more columns?
What is average value?
Max value?
Min value?
Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. 
This is called cleaning the data.

"""

# To install pandas use the command pip install pandas
# If this command fails, then use a python distribution that already has Pandas installed like,
# Anaconda, Spyder etc.

# Once Pandas is installed, import it in your applications by adding the import keyword:

# you can use an alias like pd
import pandas as pd

mydataset = {
     'cars': ["BMW", "Volvo", "Ford"],
     'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

# checking pandas version

# The version string is stored under __version__ attribute.

print(pd.__version__)