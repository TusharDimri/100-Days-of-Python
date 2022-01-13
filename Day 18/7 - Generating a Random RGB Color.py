from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.colormode(255)

direction = [0, 180, 90, 270]

def getRandomColor():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    random_color = (r, g, b)
    return random_color

def randomWalk():
    # t.speed(0)
    t.speed("fastest")
    # Code to generate Random RGB Color:
    t.fillcolor(getRandomColor())
    t.pencolor(getRandomColor())
    t.width(5)
    t.setheading(random.choice(direction))
    # We can use t.right in place of t.setheading()
    t.forward(20)
    

while True:
    randomWalk()

"""
Tuple in Python:
t = (1, 3, 6, 4)
tuple is similar to a list:
t[0], t[1], ... to access element at given index.

Unlinke lists, Tuples are immutable i.e. we cannot change the element in a tuple or add values using item assignment or remove values.
t = (1, 3, 5)
print(t)
print(type(t))
t[3] = 3 # Error
t[1] = 3 # Error

This feature of a Tuple is very useful when we want a list the doesn'nt need to be changed. For example:
The coloe scheme of your website.
"""