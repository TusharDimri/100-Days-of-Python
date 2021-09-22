def greet_with(name, location):
    print(f"Hii {name}.")
    print(f"What is it like in {location}?")

greet_with("Angela", "London")
# Here the arguments "Angela" and "London" are positional arguments.In Python, the default way of passing arguments is by using positional arguments.

greet_with(location="US", name="John")
# Here we used keyword arguments to pass arguments to the function parameters.