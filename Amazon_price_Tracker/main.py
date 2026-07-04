import requests
import lxml
from bs4 import BeautifulSoup

url = "https://amzn.in/d/0cqWmG9s"

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:152.0) Gecko/20100101 Firefox/152.0"
}

response = requests.get(url, headers=header)
content = response.text
print(response.status_code)

soup = BeautifulSoup(response.content, "lxml")

c_price = soup.find(name="span", class_="a-price-whole").getText().split(".")[0]
o_price = soup.find(name="span", class_="a-price a-text-price apex-basisprice-value").getText().split("₹")[1]

print(c_price + " -current price\n" + o_price + " -original price")
