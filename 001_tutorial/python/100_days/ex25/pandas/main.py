# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
# print(data)

# import csv
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas as pd
data = pd.read_csv("weather_data.csv")
# print(data['temp'])

# temp_list = data['temp'].to_list()
# print(temp_list)

# average = sum(temp_list) / len(temp_list)
# print("%.2f" % average)
# print(data['temp'].mean())

# print((data['temp'].max()))

print(data[data.temp == data['temp'].max()])
