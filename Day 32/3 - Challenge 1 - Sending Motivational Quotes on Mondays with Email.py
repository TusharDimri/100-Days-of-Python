import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.environ.get('MY_EMAIL')
my_password = os.environ.get('MY_PASSWORD')
to_email = os.environ.get('TO_EMAIL')

with open("quotes.txt", "r") as data:
    quotes_list = data.readlines()
    # print(quotes_list)

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    if(dt.datetime.now().weekday() == 0):
        print("Sending Email.. ")   
        random_quote = random.choice(quotes_list)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Motivational Quote\n\n{random_quote}")
        print("Sent...")

