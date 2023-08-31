import requests
from pprint import pprint

url = 'https://api.sheety.co/24921b6a05cd1a8d9a41360acd3a9af3/flightDeals (python)/prices'
response = requests.get(url=url)
# print(response.json())
# pprint(response.json())

class DataManager:
    def get_data(self):
       return response.json()['prices']       
    

