from tkinter import *


window = Tk()
window.title("My GUI Application")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # This line of code gives the specified padding to all the widgets in the window

my_label = Label(text="Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=220, y=150)
my_label.grid(column=0, row=0)

def buttonClicked():
    print("Button Clicked.")
    my_label.config(text="Button Got Clicked!")
    print(my_input.get())

my_input = Entry(width=20)
# my_input.pack()
# my_input.place(x=220, y=200)
my_input.grid(column=3, row=2)

my_button = Button(text="Click Me", command=buttonClicked)
# my_button.pack()
# my_button.place(x=220, y=250)
my_button.grid(column=1, row=1)


new_button = Button(text="New Buton", command=buttonClicked)
new_button.grid(column=2, row=0)

'''
Note:
We can't use Grid and Pack together for Layout.
'''

window.mainloop()
