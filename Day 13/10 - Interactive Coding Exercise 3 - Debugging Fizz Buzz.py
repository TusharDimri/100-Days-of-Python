# Fix the code below:-

# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

# Above code after fixing it:-

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0: # We had to use and logical operator and not or.
        print("FizzBuzz")  
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# We had if statement where there should have been elif.