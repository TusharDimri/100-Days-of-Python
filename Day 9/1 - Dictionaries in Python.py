programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary)

# Retreving items from a dictionary:-
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])

# Adding new values to the dictionary:-
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Creating an empty dictionary:-
empty_dictionary = {}

# Wiping an existing dictionary:-
# programming_dictionary = {}
# print(programming_dictionary)
    
# Edit an item in a dictionary:-
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

print("\n")

# Iterating over a dictionary:-

for key in programming_dictionary:
    print(f"key = {key} and value = {programming_dictionary[key]}")

print("\n")

for key, value in programming_dictionary.items():
    print(f"key={key} and value = {value}")

