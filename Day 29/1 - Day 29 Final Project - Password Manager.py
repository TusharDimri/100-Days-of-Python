from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

PADY = 5

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def getPassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

   
   

    password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    password_letters = [choice(letters) for char in range(randint(8, 10))]


    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)

    # print(password)

    password_entry.delete(0, END)
    password_entry.insert(index = 0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def saveData():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="OOPS", message="Please make sure that you have'nt left any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")
        if is_ok:
            with open("User Data.txt", "a") as file:
                file.write(f"{website} || {email} || {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, sticky=E, pady=PADY)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0, sticky=E, pady=PADY)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0, sticky=E, pady=PADY)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky=EW, pady=PADY)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW, pady=PADY)
email_entry.insert(0, "tushardimri@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=EW, pady=PADY)

password_button = Button(text="Generate Password", command=getPassword)
password_button.grid(row=3, column=2, pady=PADY)

add_button = Button(text="Add", width=36, command=saveData)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW, pady=PADY)


window.mainloop()