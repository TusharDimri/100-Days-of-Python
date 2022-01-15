from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=500, width=500)

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_pos = [120, 80, 40, 0, -40, -80, -120]
turtles = []

user_bet = screen.textinput(title="Make a bet: ", prompt="Which Turtle will win the race? Enter a color:")


for i in range(7):
    t = Turtle(shape="turtle")
    t.speed("slow")
    t.penup()
    t.goto(x = -230, y = y_pos[i])
    t.speed("slowest")
    # t.shape("turtle")
    turtle_color = random.choice(colors)
    colors.remove(turtle_color)
    t.color(turtle_color)
    turtles.append(t)

if user_bet:
    isRaceOn = True

while isRaceOn:
    for ts in turtles:
        random_distance = random.randint(1, 10)
        ts.forward(random_distance)

        if ts.xcor() > 230:
            winner = ts.pencolor()
            if winner == user_bet:
                print("You Won!")
            else:
                print(f"{winner.capitalize()} turtle won. You Lose.")
            isRaceOn = False


screen.exitonclick()