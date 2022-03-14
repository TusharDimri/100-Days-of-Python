#  Reading from a file:

file = open("my_file.txt", "r")
content = file.read()
print(content)
file.close()  # We should always lose a file once we open it and are done with it.

# Alternatively:
with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)
# Above syntax allows us to get rid of the additional syntx of closing the file. This helps us a lpt as we might forget it sometimes.


#  Writing to a file: 
with open("write_file.txt", "w") as file:  # Opening in write mode.
    file.write("Added using Python.")

with open("my_file.txt", "a") as file:  # Opening in append mode.   
    file.write("\nAdded using Python.")
