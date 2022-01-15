# Event Listeners
"""
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.shape("turtle")

def moveForward():
    t.forward(10)
    

screen.listen()
screen.onkey(fun = moveForward, key = "space")

screen.exitonclick();
"""

# Fucntions as Inputs:
"""
def fun_a(something):
    ...
    ...

def fun_a(fun_a):
    ...
    ...
"""

from ast import operator


def add(a, b): 
    return a+b

def subtract(a, b): 
    return a-b

def multiply(a, b): 
    return a*b

def divide(a, b): 
    return a/b

def calculate(x, y, func):
    print(func(x, y))

calculate(5, 4, add)
calculate(5, 4, subtract)
calculate(5, 4, multiply)
calculate(5, 4, divide)

# This type of functions are called Higher Order Functions. They take other functions as inputs.
# These are useful when we need to listen to events and trigger a function. 
# With methods that we have'nt created ourselves, it's recommended to use keyword arguments instead of positional arguments as shown in the example.