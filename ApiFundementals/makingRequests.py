"""
In order to make requests you have to install the package into your project.
python3 -m pip install requests

Additional resources:

request error: raise for status
https://requests.readthedocs.io/en/latest/api/#requests.Response.raise_for_status

# status code: res.status_code
"""

import requests

# res = requests.get("https://official-joke-api.appspot.com/random_joke")
# response = res.json()

# how to access specific keys in python dictionary.
# print(f"Response: {response['setup']}")
# print(f"Response: {response['punchline']}")

# ______________________________________________________

# API parameters:

# API documenation: https://sunrise-sunset.org/api

# parameters for this api:

# Request parameters
# lat (float): Latitude in decimal degrees. Required.

# lng (float): Longitude in decimal degrees. Required.

# date (string): Date in YYYY-MM-DD format.
# Also accepts other date formats and even relative date formats.
# If not present, date defaults to current date. Optional.

# callback (string): Callback function name for JSONP response. Optional.

# formatted (integer): 0 or 1 (1 is default).

# Time values in response will be expressed following ISO 8601
# and day_length will be expressed in seconds. Optional.
# tzid (string): A timezone identifier, like for example: UTC,
# Africa/Lagos, Asia/Hong_Kong, or Europe/Lisbon.
# The list of valid identifiers is available in this List
# of Supported Timezones. If provided, the times in the
# response will be referenced to the given Time Zone. Optional.

# One way to send params through get request:
# "https://api.sunrise-sunset.org/json?lat=41.554260&lng=-73.043068&date=today"

res = requests.get(
    "https://api.sunrise-sunset.org/json", params={"lat": 41.554260, "lng": -73.043068}
)
data = res.json()
print("RESP: ", data)
