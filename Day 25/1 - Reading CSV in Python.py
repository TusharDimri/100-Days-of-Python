# with open("weather_data.csv", "r") as weather_file:
#     l = weather_file.readlines()
#     print(l)

#  CSV - Comma Seperated Values.

# import csv


# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data) # Object
#     for row in data:
#         # print(row)
#         if(row[1]!='temp'):
#             print(row[1]) 


import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data)
print(data["temp"])