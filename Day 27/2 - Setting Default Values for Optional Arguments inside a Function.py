import tkinter

window  = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="This is a label", font=("Arial", 24, "bold"))
my_label.pack(side='left')

# Advanced Python Arguments:
def my_func(a = 1, b=2, c=3):  # Arguments with defualt values
    print(a, b, c)

my_func(b=3, a=2)  # Keyword Arguments

# Similar to the function given above, there are functions which have arguments which have default values. So, we can give keyword arguments for the ones we need and ignore the ones for which we want the defuat values.

window.mainloop()
'''
This main loop is like:
while True:
    listen
'''