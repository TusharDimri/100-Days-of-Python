# Absolute file parts always start off relative to the root of your computer.

#  Relative File Paths start relative to the directory we are in (also called as present woring directory or pwd).
# ../ is used to go one step back from the pwd. 
#  ./ is used if we want to look for files in the pwd.

with open("C:\\Users\\Tushar\\Desktop\\test.txt", "w") as file:
    file.write("Test.")
    print("File created successfully.")