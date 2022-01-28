from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.display()

    def display(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(x = 0, y = 270)
        self.color("white")
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"Game Over", align = ALIGNMENT, font = FONT)