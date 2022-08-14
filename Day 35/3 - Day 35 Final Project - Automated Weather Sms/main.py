import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("OPEN_WEATHER_API_KEY")
city = "Dehradun"
# lat  = 19.707911  # Test
lat  = 30.316496
# long = 83.365273  # Test
long = 78.032188
url = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_number = os.environ.get("TWILIO_NUMBER")
my_number = os.environ.get("MY_NUMBER")

params = {
    "lat":lat,
    "lon":long,
    "exclude":"current,minutely,daily",
    "appid":api_key
}

response = requests.get(url, params)
response.raise_for_status()
# print(response.json())
hourly_data = response.json()["hourly"][:12]
# print(len(hourly_data))



will_rain = False
for hour in hourly_data:
    condition_code = hour["weather"][0]["id"]
    # print(condition_code)
    if condition_code < 700:
            # print("Bring an umbrella with you.\n")
            will_rain = True

if will_rain:
    print("Bring an Umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It will rain today. Don't forget your umbrella",
                     from_=twilio_number,
                     to=my_number
                 )
else:
    print("No need to bring an Ubmbrella")
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It will not rain today. You can leave your umbrella today.",
                     from_=twilio_number,
                     to=my_number
                 )