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

def drawCircle(gap):
    t.speed('fastest')
    t.fillcolor(getRandomColor())
    t.pencolor(getRandomColor())
    t.circle(100)
    t.left(gap)

# gap = int(input("Enter gap: "))
gap = 4
for i in range(1, int(360/gap)):
    drawCircle(gap)

screen.exitonclick()