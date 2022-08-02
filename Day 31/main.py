from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
# random_index = random.randint(0, 201)
# word = ''

# ---------------------------- Card ------------------------------- #

try:
    data = pd.read_csv("data/words_to_learn.csv")
    # print(data.tail())
except:
    data = pd.read_csv("data/japanese_words.csv")
finally:
    data_dict = data.to_dict(orient="records")
    current_card = random.choice(data_dict)
# print(data_dict)

def getRandomIndex():
    # global random_index
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    # global word
    current_card = random.choice(data_dict)
    # print(current_card)
    # canvas.delete(word)
    # word = canvas.create_text(400, 263, text=current_card['Japanese'], fill="black", font=('Ariel 60 bold'))
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title, text="Japanese", fill="black")
    canvas.itemconfig(word, text=current_card["Japanese"], fill='black')
    flip_timer = window.after(3000, func=flipCard)
    
def flipCard():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")

def userKnow():
    global current_card, data
    data_dict.remove(current_card)
    data = pd.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    getRandomIndex()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="Japanese", fill="black", font=('Ariel 40 italic'))
word = canvas.create_text(400, 263, text=current_card["Japanese"], fill="black", font=('Ariel 60 bold'))
canvas.grid(column=0, row=0, columnspan=2)

flip_timer = window.after(3000, func=flipCard)


button1 = Button(image=right, highlightthickness=0, relief="flat" ,bd=0, command=userKnow)
button1.grid(row=1, column=0, pady=50)

button2 = Button(image=wrong, highlightthickness=0, relief="flat", bd=0, command=getRandomIndex)
button2.grid(row=1, column=1)

window.mainloop()