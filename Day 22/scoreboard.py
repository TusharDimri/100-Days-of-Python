from turtle import Turtle

class Scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        
    def display(self):
        self.clear()
        self.color("White")
        self.penup()
        self.hideturtle()
        # Left Player's Score:
        self.goto(-100, 200)
        self.write(self.l_score, "center", font=("Courier", 80, "normal"))
        #  Right Player's Score:
        self.goto(40, 200)
        self.write(self.r_score, "center", font=("Courier", 80, "normal"))