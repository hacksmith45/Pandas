# What is a Series?

# A Pandas Series is like a column in a table.

# It is a one-dimensional array holding data of any type.

# Create a simple Pandas Series from a list:

import pandas as pd

a = [1, 2, 3, 4]

myvar = pd.Series(a)

print(myvar)


# Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, 
# second value has index 1 etc.This label can be used to access a specified value.

print(myvar[0])

# Create labels

# With the index argument, you can name your own labels.

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)


# When you have created labels, you can access an item by referring to the label.

print(myvar["y"])


# Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

# Note: The keys of the dictionary become the labels.

# Create a Series using only data from "day1" and "day2":

calories2 = {"day1": 450, "day2": 385, "day3": 392}

myvar = pd.Series(calories2, index = ["day1", "day2"])

print(myvar)

# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

# Series is like a column, a DataFrame is the whole table.

# Create a DataFrame from two Series:

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)