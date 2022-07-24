def calculate(**kwargs):  # kwargs => Kwyword Arguments 
    print(kwargs)
    print(type(kwargs))
    print(kwargs["add"])
    for key, value in kwargs.items():
        print(f"{key}={value}")

calculate(add=3, multiply = 5)

class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        # If the given key does'nt exist in the dictionary, then get() method return none so we have optional keyword arguments.

myCar = Car(make="Nissan", model="GT-R")
print(myCar.model, myCar.make, myCar.color)