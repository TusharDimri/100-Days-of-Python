"""

API endpoint: One of the most important aspects of an API is the API endpoint. We can imagine that as a location. So we said that if we want to get data from a particular external service, we need to know what location the data is stored. For example, if we want to get money our of the bank, then we need to know the bank's address and that when it comes to API lingo, is called the API endpoint and that usually is the URL. 
For example,if we wanted to get crypto data, we might use api.coinbase.com (This is the location where coinbase data can be found). 

API request: In addition to knowing the API endpoint, we also have to make a request over the internet. This API request is kind of similar to going to the bank and trying to get some money out of their vault. For doing that we have to seek the assistance of a bank teller. This bank teller is kind of like the API beacuse it's the interface between us and the external system(bank vault in this case). We can make a number of requests to the teller which will be responded after checks and validations. If the request is valid we get a response and if not we're told to go away. 
"""

import requests

url="http://api.open-notify.org/iss-now.json"  # Location

response = requests.get(url=url) # Sending request to the location
print(response)