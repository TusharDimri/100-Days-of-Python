import pandas as pd

data = pd.read_csv("weather_data.csv")

# print(type(data)) # DataFrame(one of the 2 Pandas Data Structure)
# print(type(data["temp"])) # Series(one of the 2 Pandas Data Structure)

# data_dict = data.to_dict()
# print(data_dict)

# data_list = data["temp"].tolist()
# print(data_list)

# # print(f"Average Temperature: {sum(data_list)/len(data_list)}")  # Python Way
# print(f"Average Temperature: { data['temp'].mean() }")  # Python Pandas way

# print(data["temp"].max())

# print(data.condition)

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

def toFahrenheit(temperature):
    return (temperature * 1.8) + 32

day = data[data.day == "Monday"]
print(toFahrenheit(day.temp))

# Creating a Data Frame from scratch: 
students = {
    "students": ["Amy", "James", "John"],
    "scores": [76, 56, 65]
}

student_data = pd.DataFrame(students)
print(student_data)
student_data.to_csv("Student Data.csv")