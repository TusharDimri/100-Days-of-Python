import requests

URL = "https://api.tequila.kiwi.com/locations/query"
HEADER = {
    'apikey' : "Sec7MFnOwKGBE1dX5AISUzIYRhFI0X2I"
}

class FlightSearch:
    def getCode(self, city):
        PARAMS = {
            "term": city,
        }
        response = requests.get(url=URL, headers=HEADER, params=PARAMS)
        return response.json()["locations"][0]["code"]
        
    pass