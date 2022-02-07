from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0

    def start(self):
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-213,  260)
        self.write(f"Level: {self.level}", align="center", font= FONT)

    def levelUp(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font= FONT)

    def reset(self):
        self.level = 0
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
        time.sleep(1)
        self.clear()
        self.start()
