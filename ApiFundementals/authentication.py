"""
API authentication:


"""

import requests

url = "https://api.openweathermap.org/data/2.5/weather"
parameters = {
    "q": "Paris",
    "appid": "6e43c75c642a9923b980f2077e880777",
}

fetch = requests.get(url, params=parameters)
data = fetch.json()
print("RES: ", data)
