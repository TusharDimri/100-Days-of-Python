from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =  25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global timer
    global reps
    reps = 0
    window.after_cancel(timer)
    check.config(text="")
    my_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN  * 60

    reps += 1

    #  If it's 1st/3rd/5th/7th rep:
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        my_label.config(text="Work", fg=GREEN)
        countDown(work_sec)
    #  If it's 8th rep:
    elif reps == 8:
        my_label.config(text="Break", fg=RED)
        countDown(long_break_sec)
    #  If it's 2nd/4th/6th rep:
    elif reps == 2 or reps == 4 or reps==6:
        my_label.config(text="Break", fg=PINK)
        countDown(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countDown(count):
    global reps
    global timer
    min = math.floor(count/60)
    sec = count%60
    if sec < 10:
        sec = f"0{sec}"
    set_text = f"{min}:{sec}"
    canvas.itemconfig(timer_text, text=set_text)
    if(count!=0):
        timer = window.after(1000, countDown, count-1)
    else:
        start()
        checkmark_num = math.floor(reps/2)
        check.config(text=checkmark_num*"✔")
    

'''
Python is a strongly, dynamically typed language.
https://stackoverflow.com/questions/11328920/is-python-strongly-typed
'''


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



my_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
my_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


button1 = Button(text="Start", command=start, highlightthickness=0)
button1.grid(column=0, row=2)

button1 = Button(text="Reset", command=reset, highlightthickness=0)
button1.grid(column=2, row=2)

# ✔
check = Label(text="", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)

window.mainloop()