#  Thony editor and python tutor website have really good debuggers.

# Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# Fix the errors in the above block using thony editor or python tutor(preferred).

# Above code after fixing errors:-
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # This line was to be indented.  
  print(b_list)

mutate([1,2,3,5,8,13])

#  I used pythontutor.com to visualize this code in a debugger and then fiunf the bug and fixed it. Inside most debuggers you can put a breakpoint to sop what you're doing at this particular line. At that point you can examine what all the functions and variables are doing.