import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.environ.get('MY_EMAIL')
my_password = os.environ.get('MY_PASSWORD')
to_email = os.environ.get('TO_EMAIL')

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()  # Secures our email connection
    connection.login(user=my_email, password=my_password)
    print("Sending..")
    connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="Subject:Testing\n\nEmail body")
    print("Sent")
