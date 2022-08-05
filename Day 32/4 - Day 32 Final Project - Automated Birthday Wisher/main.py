import smtplib
import pandas as pd
import datetime as dt
import random
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.environ.get('MY_EMAIL')
my_password = os.environ.get('MY_PASSWORD')


##################### Extra Hard Starting Project ######################


# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")


# 4. Send the letter generated in step 3 to that person's email address.
def sendBestWishes(letter, to_email):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Secures our email connection
        connection.login(user=my_email, password=my_password)
        print("Sending..")
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Happy Birthday\n\n{letter}")
        print("Sent")


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def getLetter(name, email):
    print(name, email)
    random_letter = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    print(random_letter)
    with open(random_letter, "r") as letter:
        raw_letter = letter.read()
        final_letter = raw_letter.replace("[NAME]", name)
        print(final_letter)
    sendBestWishes(letter=final_letter, to_email=email)


# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
# print(today)
for i in range(len(data)):
    if(data.iloc[i, 4] == today.day and data.iloc[i, 3] == today.month):
        getLetter(name=data.iloc[i, 0], email=data.iloc[i, 1])
        # print("Happy Birthday!")
    





