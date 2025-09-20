"""
API authentication:

To get ENV Variables:
pip install python-dotenv

"""

import os
import requests

# GET ENV VAR USING SYSTEM ENVIRONMENT VARIABLES:

# api_key = os.getenv("owm_api_key")
# print(api_key)

# GET ENV VARS USING DOTENV:
# install pip install python-dotenv

# import dotenv
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("owm_api_key")
# print("API Key:", api_key)


url = "https://api.openweathermap.org/data/2.5/weather"
parameters = {
    "q": "Paris",
    "appid": api_key,
}

fetch = requests.get(url, params=parameters)
data = fetch.json()
print("RES: ", data)
