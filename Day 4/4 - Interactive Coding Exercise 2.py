"""
Who's Paying

Instructions:-
You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill. 

**Important**: You are not allowed to use the `choice()` function.

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

"""
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(names)

# print(f"{random.choice(names)} is going to buy the meal today!")

ch = random.randint(0, len(names)-1)
print(f"{names[ch]} is going to buy the meal today!")

