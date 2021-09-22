print("Welcome to the rollercoaster!")

height = float(input("Enter your height: "))

if height > 120.0:
    print("You can ride the rollercoaster!")

    age = int(input("Enter your age: "))

    if age < 12:
        bill = 5
        print(f"Ticket Cost: ${bill}.")

    elif age >= 12 and age <= 18:
        bill = 7
        print(f"Ticket Cost: ${bill}")
        
    else:
        bill = 12
        print(f"Ticket Cost: ${bill}.")
        
    photo = input("Do you want a photo taken? Press 'Y' for yes and 'N' for no: ")

    if photo == 'Y':
        # bill += 3
        # print(f"Your have to pay: {bill}")
        print(f"Your have to pay: {bill+3}")

    else:
        print(f"Your have to pay: {bill}")
        

        

else:
    print("Sorry, you have to grow taller before you ride.")
    