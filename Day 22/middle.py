from turtle import Turtle

from sqlalchemy import false

class Middle(Turtle):
    def __init__(self):
        super().__init__()

    def createMiddle(self, pos):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.goto(0, pos)
  

