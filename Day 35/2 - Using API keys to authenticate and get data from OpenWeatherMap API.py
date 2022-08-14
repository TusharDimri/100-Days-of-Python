from urllib import response
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("OPEN_WEATHER_API_KEY")
city = "Dehradun"
lat  = 30.316496
long = 78.032188
url = "https://api.openweathermap.org/data/2.5/onecall"
params = {
    "lat":lat,
    "lon":long,
    "appid":api_key
}

response = requests.get(url, params)
response.raise_for_status()
print(response.json())