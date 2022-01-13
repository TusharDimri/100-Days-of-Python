from turtle import *

jim = Turtle()
screen = Screen()
def step():
    jim.forward(100)
    jim.right(90)

for i in range(4):
    step()

screen.exitonclick()