from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.colormode(255)


direction = [0, 180, 90, 270]

def randomWalk():
    # t.speed(0)
    t.speed("fastest")
    t.fillcolor((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    t.pencolor((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    t.width(5)
    t.setheading(random.choice(direction))
    # We can use t.right in place of t.setheading()
    t.forward(20)
    

while True:
    randomWalk()

screen.exitonclick()