from cProfile import label
from tkinter import *

window = Tk()
window.minsize(width=100, height=100)
window.config(padx=10, pady=10)
window.title("Miles To Kilometres Converter")

user_input = Entry(width=20)
user_input.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

value = Label(text="0")
value.grid(column=1, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)


def buttonCliked():
    miles_value = float(user_input.get())
    km_value = miles_value * 1.609
    value.config(text=str(km_value))


button = Button(text="Calculate", command=buttonCliked)
button.grid(column=1, row=2)

window.mainloop()