# import tkinter
from tkinter import *


# window = tkinter.Tk()
window = Tk()
window.title("My GUI Application")
window.minsize(width=500, height=300)

# my_label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
my_label = Label(text="Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.pack()

# my_label['text'] = "New Text"
# my_label.config(text="This is a Label")

def buttonClicked():
    print("Button Clicked.")
    my_label.config(text="Button Got Clicked!")
    print(my_input.get())

# Entry: 
my_input = Entry(width=20)
my_input.pack()

# Button: 
# my_button = tkinter.Button()
my_button = Button(text="Click Me", command=buttonClicked)
my_button.pack()


window.mainloop()
