from time import time
import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.environ.get('MY_EMAIL')
my_password = os.environ.get('MY_PASSWORD')
to_address = os.environ.get('TO_EMAIL')

MY_LAT = 30.316496 # Your latitude
MY_LONG = 78.032188 # Your longitude


#Your position is within +5 or -5 degrees of the ISS position.



#If the ISS is close to my current position
def isISSOverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if(abs(iss_latitude-MY_LAT) <= 5 and abs(iss_longitude-MY_LONG) <= 5):
        print("ISS is close")
        return True
            
# and if it is currently dark
def isNightTime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    # print(time_now)
    if(time_now <= sunrise and time_now >= sunset):
        print("It is dark") 
        return True

# BONUS: run the code every 60 seconds.
while True:
    if isISSOverhead() and isNightTime():
        # Then send me an email to tell me to look up.
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_address,
            msg="Subject:Look Up 👆\n\nThe ISS is above you."
        )
    
    time.sleep(60)


