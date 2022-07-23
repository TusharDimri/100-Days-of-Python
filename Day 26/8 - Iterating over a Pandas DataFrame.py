students = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping Through / Iterating over a Dictionary:
for(key, value) in students.items():
    print(value)

import pandas

students_data_frame = pandas.DataFrame(students)
print(students_data_frame)

# Looping Through / Iterating over a DataFrame:

# Method 1(Not Preferred):
# for key,value in students_data_frame.items():
#     print(f"{key}:{value}")

# Method 2:
# Looping through the rows of a DatFrame:
for (index, row) in students_data_frame.iterrows():
    print(f"{index}:{row}")