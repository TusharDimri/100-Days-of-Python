from urllib import response
import requests

parameters = {
    "amount": 10,
    "type":"boolean"
}

url = "https://opentdb.com/api.php"

response = requests.get(url=url, params=parameters)

response.raise_for_status()
data = response.json()


# print(data)

question_data = data["results"]

# print(question_data)
