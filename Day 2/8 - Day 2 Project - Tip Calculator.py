print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? ₹"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))

people = int(input("How many people to split the bill?"))

total_bill =  bill + ((tip/100) * bill)

split = total_bill / people
# split = round(split, 2)
split = "{:.2f}".format(split)

print(f"Each person should pay ₹{split}")