import requests
import datetime

URL = "https://api.tequila.kiwi.com/v2/search"
HEADER = {
    'apikey' : "Sec7MFnOwKGBE1dX5AISUzIYRhFI0X2I"
}
today = datetime.date.today()
date_from = today + datetime.timedelta(days=1)
date_to = date_from+datetime.timedelta(days = 6*30)



class FlightData:
    def  getFlightData(self, city):
        PARAMS = {
            'fly_from': 'LON',
            'fly_to': city,
            'max_stopvers': 0,
            'currency': 'GBP',
            'date_from': f"{str(date_from).split('-')[2]}/{str(date_from).split('-')[1]}/{str(date_from).split('-')[0]}",
            'date_to': f"{str(date_to).split('-')[2]}/{str(date_to).split('-')[1]}/{str(date_to).split('-')[0]}",
            'flight_type': 'round',
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28
        }
        response = requests.get(url=URL, params=PARAMS, headers=HEADER)
        return(response.json()["data"])


