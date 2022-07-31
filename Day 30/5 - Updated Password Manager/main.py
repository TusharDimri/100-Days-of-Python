from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
from cv2 import TermCriteria_COUNT
import pyperclip
import json

"""
Write JSON:
json.dump()

Read JSON:
json.load()

Update JSON:
json.update()
"""

PADY = 5

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def getPassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

   
   

    password_list = []

    password_letters = [choice(letters) for char in range(randint(8, 10))]

    password_symbols = [choice(symbols) for char in range(randint(2, 4))]

    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(index = 0, string=password)
    pyperclip.copy(password)

# -------------------------------- Search ---------------------------------- #

def search():
    to_search = website_entry.get()
    if len(to_search) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure that you have entered the username or website to search for.")
    else:
        try:
            with open("User Data.json", "r") as file:
                dict_to_search = json.load(file)
        except Exception as e:
            messagebox.showinfo(title="OOPS", message=f"No Data File Found.")
        else:
            # try:
            #     info = dict_to_search[to_search]
            # except Exception as e:
            #     pass
            # else:
            #     messagebox.showinfo(title=to_search, message=f"Email: {info['email']}\nPassword: {info['password']}")
            #     website_entry.delete(0 ,END)

            if to_search in dict_to_search:
                info =dict_to_search[to_search] 
                messagebox.showinfo(title=to_search, message=f"Email: {info['email']}\nPassword: {info['password']}")
            else:
                messagebox.showinfo(title=to_search, message=f"No such record exist.")

                
    


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
            data_dict = {
                website: {
                    "email":email,
                    "password":password,
                }
            }
            try:
                with open("User Data.json", "r") as file:
                    # Reading the old data
                    data = json.load(file)


            except Exception as e:
                with open("User Data.json", "w") as file:
                    json.dump(data_dict, file, indent=4)

            else:
                # Updating the old data with new data
                data.update(data_dict)
                with open("User Data.json", "w") as file:
                    json.dump(data, file, indent=4)


            finally: 
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

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky=EW, pady=PADY)
website_entry.focus()

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky=EW, pady=PADY)

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