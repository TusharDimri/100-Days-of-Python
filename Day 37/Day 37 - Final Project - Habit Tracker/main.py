from json import load
from datetime import datetime
from turtle import update
from urllib import response
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN")
USERNAME = "tushar29dimri"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Knowledge",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
    "timezone": "Asia/Kolkata",
}
# HTTP Header:
headers = {
    "X-USER-TOKEN":TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Post Request: 
def postPixel(username, graphId, token):
    today = datetime.now()
    url = f"https://pixe.la/v1/users/{username}/graphs/{graphId}"
    config={
        "date": today.strftime("%Y%m%d"),
        "quantity":"4",
    }
    headers = {
        "X-USER-TOKEN":token
    }
    response = requests.post(url=url, json=config, headers=headers)
    print(response.text)

# Put Reuqest: 
def updatePixel(username, graphId, token, date):
    url = f"https://pixe.la/v1/users/{username}/graphs/{graphId}/{date}"
    config = {
        "quantity":"3"
    }
    headers = {
        "X-USER-TOKEN":token
    }
    response = requests.put(url=url, json=config, headers=headers)
    print(response.text)

# Delete Request: 
def deletePixel(username, graphId, token, date):
    url = f"https://pixe.la/v1/users/{username}/graphs/{graphId}/{date}"
    headers = {
        "X-USER-TOKEN":token
    }
    response = requests.delete(url=url, headers=headers)
    print(response.text)



postPixel(USERNAME, graph_config["id"], TOKEN)
# updatePixel(USERNAME, graph_config["id"], TOKEN, datetime.now().strftime("%Y%m%d"))
# deletePixel(USERNAME, graph_config["id"], TOKEN, datetime.now().strftime("%Y%m%d"))
