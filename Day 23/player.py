from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def moveUp(self):
        self.forward(MOVE_DISTANCE)

    def hasWon(self):
        if self.distance(0, FINISH_LINE_Y) < 5:
            self.goto(STARTING_POSITION)
            return True

    def hasLost(self, cars):
        for car in cars:
            if self.distance(car) < 30:
                self.goto(STARTING_POSITION)
                return True


