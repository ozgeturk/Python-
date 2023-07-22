# DATA MANIPULATION WITH PANDAS

import pandas as pd
import numpy as np

last_year = pd.read_csv("employee_revenue_lastyear.csv")

print(last_year.head(8))
print(last_year.tail())

print(last_year.shape)

print(last_year.info())

last_year["Year"] = 2021 # adding column called "Year"

print(last_year)

names = np.array(['Ben', 'Omer', 'Karen', 'Celine', 'Sue', 'Bora', 'Rose', 'Ellen', 'Bob', 'Taylor,', 'Jude'])
number_of_calls = np.array([300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80])
average_deal_sizes = np.array([8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12])
revenues = np.array([2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500])

dictionary = {"name": names,
              "calls": number_of_calls,
              "avg_deal_sizes": average_deal_sizes,
              "revenues": revenues}

current_year = pd.DataFrame(dictionary)
print(current_year.head())

current_year["Year"] = 2022
print(current_year.head())

print(last_year.head())

current_year.columns = last_year.columns # to assignn same name of columns

all_data = pd.concat([last_year, current_year], axis=0) # axis=0 means that we merge them by rows
print(all_data)


print(all_data.reset_index(drop=True, inplace=True))

print(all_data.isna().any()) # to check is there any missing values, we use isna

#print(all_data.fillna(value=np.mean(all_data), inplace=True)) #inplace must be true to make data frame be updated

print(all_data.drop_duplicates(inplace=True))

all_data.reset_index(drop=True)

all_data.describe()

all_data[all_data["Year"] == 2021].describe()
all_data[all_data["Year"] == 2022].describe()

all_data.sort_values(by="Revenue")

print(all_data[all_data["Year"] == 2022]. sort_values(by="Revenue"))

print(all_data["Name"].value_counts())