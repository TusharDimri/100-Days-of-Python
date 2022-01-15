from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def moveForward():
    t.forward(10);

def moveBackward():
    t.backward(10);

def moveClockwise():
    t.right(10);

def moveAntiClockwise():
    t.left(10);

def clearDrawing():
    t.clear()
    t.reset()

screen.listen()

screen.onkey(fun=moveForward, key="w");
screen.onkey(fun=moveBackward, key="s");
screen.onkey(fun=moveClockwise, key="a");
screen.onkey(fun=moveAntiClockwise, key="d");
screen.onkey(fun=clearDrawing, key="c");

screen.exitonclick()