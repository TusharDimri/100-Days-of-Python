"""
There are different response codes with different meanings but the most important thing they tell us is if our request succeeded or if it failed.
We can summarise these code just by looking at the first number:
1XX : Hold On.
2XX : Here You Go (Success).
3XX : Go Away (No permission).
4XX : You Screwed Up.
5XX : I(The server) Screwed Up.
"""


import requests

url="http://api.open-notify.org/iss-now.json"  # Location

response = requests.get(url=url) # Sending request to the location
# print(response)
print(response.status_code)

# Not the correct way to do things:
# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")

response.raise_for_status()  # Raise correct exception.

data = response.json()
print(data)
print(data["iss_position"])