# Note: 0 => True and 1 = >False

print("Logical and:-")
print(0 and 0)
print(0 and 1)
print(1 and 0)
print(1 and 1)

print("Logical or:-")
print(0 or 0)
print(0 or 1)
print(1 or 0)
print(1 or 1)

print("Logical not:-")
print(not 0) # Can be written as: !0
print(not 1) # Can be written as: !1

"""
age = 18
if age >= 12 and age <= 25:
    print("Condition Satisfied") 
if age == 18 or age == 19:
    print("Condition Satisfied")
"""

print("Welcome to the rollercoaster!")

height = float(input("Enter your height: "))
bill = 0

if height > 120.0:
    print("You can ride the rollercoaster!")

    age = int(input("Enter your age: "))

    if age < 12:
        bill = 5
        print(f"Ticket Cost: ${bill}.")

    elif age >= 12 and age <= 18:
        bill = 7
        print(f"Ticket Cost: ${bill}")

    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
        
    else:
        bill = 12
        print(f"Ticket Cost: ${bill}.")
        
    photo = input("Do you want a photo taken? Press 'Y' for yes and 'N' for no: ")

    if photo == 'Y':
        # bill += 3
        # print(f"Your have to pay: {bill}")
        print(f"Your have to pay: ${bill+3}")

    else:
        print(f"Your have to pay: ${bill}")
        

        
else:
    print("Sorry, you have to grow taller before you ride.")
    