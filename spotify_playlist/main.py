import requests
from bs4 import BeautifulSoup


# year = input("Which year do you want to travel to? ")

year = "2024" 

print("Let's go to the year " + year)

url = f"https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_top-ten_singles_in_{year}"
print(url)

response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, "html.parser")

print(content)
