
"""
array = np.array([1,2,3,4,5])

print(type(array)) """

names = ['Ben', 'Omer', 'Karen', 'Celine', 'Sue', 'Bora', 'Rose', 'Ellen', 'Bob', 'Taylor,', 'Jude']
number_of_calls = [300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80]
average_deal_sizes = [8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12]
revenues = [2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500]

import numpy as np

data = np.array([], dtype=int) #data type integer, defaults float
print(data)

def append_names(names_list):
    global data
    for i in names_list:
        data = np.append(data, names.index(i))

def append_performance_measures(feature_list):
    global data
    data = np.append(data, feature_list)

append_names(names)
append_performance_measures(number_of_calls)
append_performance_measures(average_deal_sizes)
append_performance_measures(revenues)

print(data)
print(data.shape)

data = data.reshape(4, 11) # 4 rows - 11 columns
print(data)
print(data.shape)

print(data[0]) # to reach rows

print(data[3,7]) # the value in 3rd row 7th column

def calculate_performance(employee_name):
    idx = names.index(employee_name)
    number_of_calls = data[1, idx]
    average_deal_sizes = data[2, idx]
    revenues = data[3, idx]

    score = (average_deal_sizes*revenues)/number_of_calls

    return score

print(calculate_performance("Ellen"))

performance_scores = []
for name in names:
    score = int(calculate_performance(name))
    performance_scores.append(score)

data = np.concatenate((data, [performance_scores]), axis=0) # axis=0 indicates vertical axis, axis=0 indicates horizontal

print(data)

idx_best_employee = np.argmax(data[4]) # 4th row
idx_worst_employee = np.argmin(data[4])

print(f"Best performing employee: {names[idx_best_employee]}")
print(f"Worst performing employee: {names[idx_worst_employee]}")

