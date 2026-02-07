import requests
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

parameters = {
    "lat": "28.61",
    "lon": "77.23",
    "appid": os.environ.get("OWM_APPID")
}

response  = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
print(response.raise_for_status())

print(response.json())
