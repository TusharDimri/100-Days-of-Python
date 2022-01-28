class Animal():
    def __init__(self, ):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal): # Fish Inherits from Animal Class
    def __init__(self):
        super().__init__()
        # super refers to the super class which in this case is Animal Class.
        # Above code allows Fish Class to inherit the Attributes and Methods of Animal Class(it's super class).

    def breathe(self):
        super().breathe()
        print("Doing this underwater")

    def swim(self):
            print("Moving in Water")

nemo = Fish()

nemo.swim()
nemo.breathe() # Method that we inherited from class Animal but we modified it in Fish Class.

print(nemo.num_eyes) # Attribute which we inherited from class Animal.