import random
from turtle import Turtle, Screen

colors = [(242, 250, 247), (252, 244, 248), (239, 244, 249), (220, 152, 106), (132, 172, 197), (215, 131, 149),
          (225, 69, 88), (24, 119, 154), (239, 209, 99), (123, 178, 151), (37, 122, 85), (20, 167, 204), (216, 85, 76),
          (144, 83, 58), (148, 70, 90), (237, 161, 176), (240, 165, 151), (43, 164, 128), (171, 151, 72),
          (176, 185, 216), (160, 209, 173), (3, 92, 113), (27, 57, 80), (27, 89, 60), (238, 219, 6), (51, 58, 91),
          (151, 208, 219), (100, 125, 177), (71, 75, 42)]

t = Turtle()
screen = Screen()
screen.colormode(255)
t.speed('fastest')

def changeInitialPosition():
    t.hideturtle()
    t.penup()
    t.goto(-250, -200)
    t.showturtle()
    t.pendown()

def startAgain():
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(500)
    t.right(180)

def setRandomColor():
    t.fillcolor(random.choice(colors))
    t.pencolor(random.choice(colors))

def draw():
    t.pendown()
    t.dot(20)
    t.penup()
    t.forward(50)

changeInitialPosition()
for i in range(10):
    if i != 0:
        startAgain()
    for j in range(10):
        setRandomColor()
        draw()
        if i == 9 and j == 9:
            t.hideturtle()

screen.exitonclick()