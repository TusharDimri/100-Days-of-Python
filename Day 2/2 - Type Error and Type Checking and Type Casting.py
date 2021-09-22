# len(123) will give an error, type error specifically

# To know the Data Type of a \Constant or a Variable, we use type() function
print(type("Tushar"))

name = input("Enter your name: ")
print(type(name))
print(type(len(name)))


# Type Conversion / Type Casting

nm = "Tushar Dimri"
l = len(nm) # Type casting integer value to a string
print("Your name has " + str(l) + " Characters")

a = 123
print(type(a))
a = float(a)
print(type(a)) 

print(70 + float("100.5"))