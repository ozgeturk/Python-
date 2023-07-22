# with pandas : load - analyze - manipulate data

import pandas as pd

# Pandas series - can hold any type of value

my_series = pd.Series([10, 27, 32, 41, 5])

print(my_series.size)
print(my_series.ndim)
print(my_series.head(2))
print(my_series.tail(2))

print(my_series[2])
print(my_series[1:4])

numbers = [[1, 2, 39, 67, 90], [1, 2, 39, 67, 90]]

df = pd.DataFrame(numbers)
print(df)
import numpy as np
arr = np.array([[1,2,39,67,90], [8,12,45,12,8], [2, 8, 34, 90, 102]])
df = pd.DataFrame(arr)
print(df.describe())
print(df.describe().T) # T transpose the data changes columns to rows,to read easily

# export data from different sources: CSV, TXT, XLSX

dataframe_csv = pd.read_csv("file.csv")
dataframe_txt = pd.read_csv("file.txt")
dataframe_xlsx = pd.read_xlsx("file.xlsx")



