'''
#  Some common errors:

# File not found:
with open("file.txt", "r") as file:  # No such file in Present Working Directory (Error)
    print(file.readlines())

# Key Error:
dict = {"key":"value"}
print(dict["keey"])  # No such key exist.

# Index Error:
l = [1,2,3]
print([4])

# Type Error:
print("abc" + 1)


Exception Handling Syntax:

try:
    pass
    # Something that might cause an exception.

except Exception as e:
    pass
    # Do this if there was an exception.

else:
    pass
    # Do this if there were no exceptions.

finally:
    pass
    # Do this no matter what happens

'''

try:
    with open("file.txt", "r") as f:
        print(f.readlines())
    dict = {"key":"value"}
    print(dict["keeey"]) 


# except Exception as e:
    # print(f"Error:\n{e}")

except FileNotFoundError as err:
    # As no such file exist (problem) we'll create a new file (solution).
    # file = open("file.txt", "w")
    print(err)

except KeyError as err:
    dict["keey"] = "value"
    print(err)
     
else:
    print("Done with the lesson")

finally:
    print("Keep Hustling")

