from turtle import Screen, Turtle
import random

t = Turtle()
screen = Screen()
screen.colormode(255)

angles = [120, 90, 72, 60, 51.4, 45, 40, 36]


def basicSteps(angle):
    t.right(angle)
    t.forward(100)

for i in range(3, 11):
    t.fillcolor((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    t.pencolor((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    for j in range(i):
        # Anglea's Logic:
        # basicSteps(360/i)
        # My Logic(Uses angles list):
        basicSteps(angles[i-3])



screen.exitonclick()
