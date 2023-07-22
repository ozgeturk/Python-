
# DATA VISUALIZATION
import matplotlib.pyplot as plt
import pandas as pd
"""
# Line Plot
x = [0, 2, 4, 6, 8, 10, 12, 14, 16]
y = [0, 4, 16, 36, 64, 100, 144, 196, 256]
plt.plot(x,y)
plt.title("Example data - Line plot")
plt.show() # to show graph

# Scatter Plot

plt.scatter(x,y)
plt.title("Example data- scatter plot")
plt.show()

# Bar Chart

plt.bar(x,y)
plt.title("Example data - Bar Chart")
plt.show()

# SUB PLOT : Helps to see the graphs side by side

fig = plt.figure(figsize=(18, 5)) #Figure object's size 18x5

first_plot = fig.add_subplot(1,3,1)
first_plot = fig.add_subplot(1,3,1)
first_plot.plot(x,y,color="red")
first_plot.set_title("Example data - Line plot")

second_plot = fig.add_subplot(1,3,2)
second_plot.scatter(x,y, color = "green")
second_plot.set_title("Example data - Scatter Plot")

third_plot = fig.add_subplot(1,3,3)
third_plot.bar(x,y, color = "orange")
third_plot.set_title("Example data - Bar Chart")

plt.show()
"""

data = pd.read_csv("employee_performance.csv")

print(data.head())

education_level = data["Education"].value_counts()
print(education_level)

plt.pie(education_level, labels=education_level.index)
plt.show()

plt.bar(data["Name"], data["Revenue"])
plt.show()

plt.bar(data["Name"], data["Revenue"], label = "Revenues")
plt.bar(data["Name"], data["Number of Calls"], label = "Number of Calls")

plt.legend() # to differentiate btw data, we add legend
plt.grid()
plt.show()
