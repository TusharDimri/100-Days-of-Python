from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.display()

    def display(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(x = 0, y = 270)
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.set_high_score(self.score)
            self.high_score = self.get_high_score()
        self.score = 0
        self.display()

    def get_high_score(self):
        with open("data.txt", "r") as file:
            return int(file.read())

    def set_high_score(self, new_score):
        with open("data.txt", "w") as file:
            file.write(str(new_score))