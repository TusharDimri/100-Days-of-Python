from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles = []

    def createPaddle(self, pos):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(pos)
        # self.paddles.append(paddle)

    def moveUp(self):
        # paddle = self.paddles[0]
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def moveDown(self):
        # paddle = self.paddles[0]
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        
        
        