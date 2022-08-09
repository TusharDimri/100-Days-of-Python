"""
Apart from endpoints, APIs also have parameters and this is a way that allows us to give an input when we are making an API request.
Coming back to our bank analogy, that's kinda similar to going to the bank and instead of just asking them about their opening hours, sort of a broad stroke question, we can pass a parameter like askig them their closing time for Monday and this allow sus to get specific pice of information that we're interested in depending on the input that we provided as a parameter. Not all APIs have parameters and some are increadibly simple like the ISS Location API but other ones allow us to provide parameters.    
"""

import requests
from datetime import datetime

MY_LAT = 30.316496
MY_LONG = 78.032188

url = "https://api.sunrise-sunset.org/json"
parameters = {
    "lat" : MY_LAT, 
    "lng" : MY_LONG,
    "formatted" : 0
}


response = requests.get(url=url, params=parameters, verify=False)
response.raise_for_status()
data=response.json()
# print(data)
print(data["results"]["sunrise"].split("T")[1].split(":")[0])
print(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)
