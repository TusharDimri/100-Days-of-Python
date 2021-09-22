print("Welcome to the rollercoaster!")

height = float(input("Enter your height: "))

if height > 120.0:
    print("You can ride the rollercoaster!")

    age = int(input("Enter your age: "))

    if age < 12:
        print("Please pay $5.")

    elif age >= 12 and age <= 18:
        print("Please pay $7")
        
    else:
        print("Please pay $12.")
        

else:
    print("Sorry, you have to grow taller before you ride.")
    