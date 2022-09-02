from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
AUTHORIZATION_HEADER = os.environ.get("AUTHORIZATION_HEADER")

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}

data = {
    "query":input("What exercises did you do today? ")
}
response = requests.post(url=url, json=data, headers=headers)
workout_data = response.json()["exercises"]

sheet_url = "https://api.sheety.co/24921b6a05cd1a8d9a41360acd3a9af3/myWorkouts/workouts"
sheet_headers = {
    "Authorization" : AUTHORIZATION_HEADER
}
# print(workout_data)
for exercise in workout_data:
    # print(exercise)
    workouts = {
        "workout":{
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise":str(exercise['name']).title(),
            "duration":exercise['duration_min'],
            "calories":exercise['nf_calories'],
        }
    }
    print(workouts)
    sheet_response = requests.post(url=sheet_url, json=workouts, headers=sheet_headers)
    print(sheet_response.text)
