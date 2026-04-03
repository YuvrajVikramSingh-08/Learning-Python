import requests
import os
from dotenv import load_dotenv
load_dotenv()

url_get = "https://api.sheety.co/b0c798dac0fad5f0c8af9f040762901c/flightDeals/prices"

response = requests.get(url_get)
# print(response.json())
# print(response.json()['prices'])

class DataManager:
    def __init__(self):
        self.data = response.json()['prices']

    def post(self, sheet):
        self.data = sheet
        for i in self.data:
            rid = i["id"]
            data = {"price": {
                    "iataCode": i["iataCode"],
                }
            }
            print(data)
            print(rid)
            url_post = f"https://api.sheety.co/b0c798dac0fad5f0c8af9f040762901c/flightDeals/prices/{rid}"
            response_p = requests.put(url_post, json=data)
            print(response_p.status_code)
