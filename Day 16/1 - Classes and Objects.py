# Object has Attributes(Variables) and Methods(Functions)
import turtle
from turtle import Turtle, Screen
# import turtle
# import One

# print(One.var)
# timmy = turtle.Turtle()  # Creating a new Turtle Object

timmy = Turtle()  # Creating a new Turtle Object
my_screen = Screen()  # Creating a Screen Object

print(timmy)

#  Object Attributes:
print(my_screen.canvheight)
print(my_screen.canvwidth)

# Object Methods:
timmy.shape("turtle")  # shape() is a method from Turtle class
timmy.color("DeepSkyBlue")
timmy.fd(100)
my_screen.exitonclick()  # exitonclick() is a method from Screen class
