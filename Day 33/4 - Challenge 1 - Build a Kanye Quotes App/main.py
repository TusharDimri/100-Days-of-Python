from tkinter import *
import requests
kanye_quote = "Quote"


def get_quote():
    url = "https://api.kanye.rest"
    data = requests.get(url)
    # print(data)
    global kanye_quote
    kanye_quote = str(data.json()["quote"])
    # print(kanye_quote) 
    canvas.itemconfig(quote_text, text=kanye_quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=kanye_quote, width=250, font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, relief="flat", command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()