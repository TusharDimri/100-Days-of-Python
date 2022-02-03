from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def createBall(self):
        self.shape("circle")
        self.speed(1)
        self.penup()
        self.color("white")
        self.goto(0, 0)

    def move(self):
        self.speed("slowest")
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.x_move *= -1
        
        