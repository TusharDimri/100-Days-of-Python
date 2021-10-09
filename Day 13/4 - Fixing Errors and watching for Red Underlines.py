# Uncomment below code and Fix the Errors 

# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# When the editor is giving you an error or the console is giving you an error, fix all the errors before you continue. This is easier with editors as the errors are highlited with a red line(usually). 

# Above code after fixing the errors:-

age = int(input("How old are you? ")) 
# Earlier we were not converting our string to integer and we were comparing strings(from input) with 18(integer).
if age >= 18:
    print(f"You can drive at age {age}.")  # This line was not indented so it was a syntax error.
    # Also we forgot to change the string to an f string so we were not getting expected output.

# Note:-
# If you don't know why you're getting an error then Goggle it. Experience comes really handy with debugging and t=you become better as you solve more errors and fix more bugs. 