"""
Write a program that switches the values stored in the variables a and b :-  

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇




#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

"""

a = input("a: ")
b = input("b: ")

'''
Method 1 :-
temp = a 
b =temp
'''

# Method 2(More Pythonic Way):- 
a , b = b , a

print("a: " + a)
print("b: " + b)
