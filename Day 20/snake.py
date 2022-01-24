#  3 - Create a Sanke Class and Move to OOP

from turtle import Turtle, Screen
import time

screen = Screen()

STARTING_POSITIONS = [(0, 0), (-10, 0), (-30, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]


    def createSnake(self):
                for position in STARTING_POSITIONS:
                    new_segment = Turtle("square")
                    new_segment.color("white")
                    new_segment.penup()
                    new_segment.goto(position)
                    self.segments.append(new_segment)

    def move(self):
        screen.update()
        time.sleep(0.1)
        for index in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[index-1].xcor()
            new_y = self.segments[index-1].ycor()
            self.segments[index].goto(new_x, new_y) 

        self.head.forward(DISTANCE)

    # 4 - Controlling the Snake with a Keypress(Callback Functions)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
        