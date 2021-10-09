# Pretend to be the Computer and evalute each line to find bugs.

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# Evaluate the code above by plaing Computer.


# Code after fixing bug:-
year = int(input("What's your year of birth? "))
if year > 1980 and year <= 1994: # Bug was here
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# The bug wa that year = 1994 was doing nothing. I solved it by playing computer and describing the problem and also checking what the computer will print for different values of year.