from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def createCar(self):
        if random.randint(1, 7) == 1:
            self.hideturtle()
            car = Turtle("square")
            car.penup()
            new_y =  random.randint(-250, 260)
            car.goto(260, new_y)
            # print(new_y)
            car.shapesize(stretch_len=3, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.setheading(180)
            self.cars.append(car)
    
    def moveCars(self):
        # print(self.cars)
        for car in self.cars:
            car.forward(self.speed)
                   
    def increaseSpeed(self):
        self.speed += MOVE_INCREMENT
            