import turtle
import pandas as pd
from sqlalchemy import false

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

# To get co-ordinates from Turtle Screen:
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

states_data = pd.read_csv("50_states.csv")
# print(states_data[states_data["state"] == "Texas"]["x"])

user_answer = screen.textinput(title="Guess the state", prompt="Name a U.S. state").lower()


guessed_states = []

while len(guessed_states) < 50:
    if(user_answer == "exit"):
        break

    for state in states_data["state"]:
        if str(state).lower() == user_answer:
            x_coor = int(states_data[states_data["state"] == state]["x"])        
            y_coor = int(states_data[states_data["state"] == state]["y"]) 
            guessed_states.append(state)
            # print(x_coor)
            # print(y_coor)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            # turtle.setposition(x_coor, y_coor)
            t.goto(x_coor, y_coor)
            t.write(state, align="center", move=False)
            t.home()


    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Name a U.S. state").lower()

states_to_learn = []
# for state in states_data["state"]:
#     if state not in guessed_states:
#         states_to_learn.append(state)
states_to_learn = [state for state in states_data["state"] if state not in guessed_states]

states_to_learn_dict = {
    "state":states_to_learn 
}
        
states_to_learn_df = pd.DataFrame(states_to_learn_dict)
states_to_learn_df.to_csv("States To Learn.csv")

# screen.exitonclick()
# turtle.mainloop()