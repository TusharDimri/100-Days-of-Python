#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

url = 'https://api.sheety.co/24921b6a05cd1a8d9a41360acd3a9af3/flightDeals (python)/prices'


data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager =  NotificationManager()

data = data_manager.get_data()

for d in data:
    if d['iataCode'] == '':
        u = f"{url}/{d['id']}"
        body = {
            'price': {
                'iataCode': flight_search.getCode(d['city'])
            }
        }
        # pprint(body)
        response = requests.put(url=u, json=body)
        print(response.json())

for d in data:
    city = flight_search.getCode(d['city'])
    # print(f"{d['city']}: £{flight_data.getFlightData(city)}")
    if flight_data.getFlightData(city)[0]['price'] < d["lowestPrice"]:
        notification_data = {
            'price' : flight_data.getFlightData(city)[0]['price'],
            'cityFrom' : flight_data.getFlightData(city)[0]['cityFrom'],
            'flyFrom' : flight_data.getFlightData(city)[0]['flyFrom'],
            'cityTo' : flight_data.getFlightData(city)[0]['cityTo'],
            'flyTo' : flight_data.getFlightData(city)[0]['flyTo'],
            'departure_date' : str(flight_data.getFlightData(city)[0]['route'][0]['local_departure'])[0:10],
            'arrival_date' : str(flight_data.getFlightData(city)[0]['route'][0]['local_arrival'])[0:10],
        }
        notification_manager.sendNotification(**notification_data)

