"""
Syntax:

new_dict = {new_key:new_value for item in list}
new_dict = {new_key:new_value for item,value in dict.items()}
"""
import random

names = ["Alex", "James", "Mia", "John", "Steve"]
student_score = {name:random.randint(1, 100) for name in names}
print(student_score)

student_score  = {
    "Alex" : 62,
    "James": 78,
    "Mia": 67,
    "John": 91,
    "Steve": 88
}

passed_students = {student:marks for (student, marks) in student_score.items() if marks>=70}
print(passed_students)