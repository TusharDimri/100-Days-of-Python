from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def dashedLine():
    tim.pendown()
    tim.forward(4)
    tim.penup()
    tim.forward(4)

for i in range(50):
    dashedLine()


tim.shape("turtle")



screen.exitonclick()