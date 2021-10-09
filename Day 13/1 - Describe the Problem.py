# Describe Problem

def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")

my_function()

# i will store values from 1 to 19. 20 is not included. in the if condition we check i for 20 but i never stores the value 20 so nothing is printed. 

# Fix for above bug:-

def my_function_fixed():
    for i in range(1, 21):
        if i == 20:
            print("You got it")
    
my_function_fixed()


# Always whenever you come across a problem in your code, try to describe it so that you really understand what the issue is and then test your assumptions and see which of those assumptions is really false.