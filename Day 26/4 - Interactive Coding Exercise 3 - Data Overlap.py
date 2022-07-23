# Instructions

"""
Take a look inside **file1.txt** and **file2.txt**. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files. 

e.g. if file1.txt contained:
"""

'''
1
'''

'''
2
'''

'''
3
'''

'''
and file2.txt contained:
'''

'''
2
'''

'''
3
'''

'''
4
'''

'''
result = [2, 3]
'''

# **IMPORTANT**: The result should be a list that contains **Integers**, not **Strings**. Try to use **List Comprehension** instead of a **Loop**.

with open("file1.txt", "r") as file1:
    file1_data = file1.readlines()
    file1_data = [int(data) for data in file1_data]

with open("file2.txt", "r") as file2:
    file2_data = file2.readlines()
    file2_data = [int(data) for data in file2_data]

# print(file1_data)
# print(file2_data)

intersection = [data for data in file1_data if data in file2_data]
print(intersection)