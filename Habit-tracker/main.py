import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = "yuvraj08"
TOKEN = os.getenv("PIXELA_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = dt.datetime.now().strftime("%Y%m%d")

pixel_config = {
    "date": today,
    "quantity": "1"
}

response = requests.post(url=post_endpoint, json=pixel_config, headers=headers)
print(response.text)
