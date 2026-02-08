import requests
import os
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
API_ENDPOINT_STOCK = "https://www.alphavantage.co/query"
parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("ALPHA_API_KEY")
}

NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
news_params = {
    "apikey": NEWS_API_KEY,
    "q": COMPANY_NAME,
}

def check_price_diff(daily_data, news):
    last_day = []
    counter = 1
    for i in daily_data:
        if counter < 3:
            last_day.append(i)
            counter += 1
        else:
            break

    yesterday_closing = float(daily_data[last_day[0]]['4. close'])
    before_yesterday_calling = float(daily_data[last_day[1]]['4. close'])

    diff = (yesterday_closing - before_yesterday_calling)
    percent = diff*100/before_yesterday_calling

    if diff > 0:
        if diff > (5*before_yesterday_calling/100):
            print("Increased")
            percent = diff*100/before_yesterday_calling
    else:
        if (diff*-1) > (5*before_yesterday_calling/100):
            print("Decreased")
            percent = diff * 100 / before_yesterday_calling

    print(f"{percent}%  value change.")
    for i in news:
        print(i)

response_news = requests.get(url=NEWS_ENDPOINT, params=news_params)
news_data = response_news.json()["articles"]

top_news = [headlines['title'].split(" | ")[0] for headlines in news_data[:3]]

response_stocks = requests.get(url=API_ENDPOINT_STOCK, params=parameters_stock)
data = response_stocks.json()["Time Series (Daily)"]
print(data)

check_price_diff(daily_data=data, news=news_data)