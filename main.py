
from newsapi import NewsApiClient
import requests
from alpha_vantage.timeseries import TimeSeries
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


api_key= "JF0NC3VXZWSUHH2Q."

stock_p={"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol" : STOCK_NAME,"apikey": api_key}



response=requests.get(STOCK_ENDPOINT, params=stock_p)

# print(response.json())

data1=float(response.json()["Time Series (Daily)"]["2022-12-20"]["4. close"]) #yesterday

data2=float(response.json()["Time Series (Daily)"]["2022-12-16"]["4. close"]) #the day before yesterday

diff= abs((data1)-(data2))

if (diff/data2)*100>5:
  print("Get News")

print(data2)
print(data1)
print("diff ", diff)


news_api_key="8aaf269886c74be8af73982458aedb9b"
news_parameter={
  "apiKey": news_api_key,
  "qInTitle": COMPANY_NAME,
  "language": 'en'
}

news_response = requests.get(NEWS_ENDPOINT, params=news_parameter)

three_articles=news_response.json()["articles"]

formatted_articles=[f"Headline: {article['title']} \nBrief: {article['description']} "   for article in three_articles]

print(formatted_articles)

sid="AC8fc4310e86dda31cecd2c38fb6652513"
auth_token="73d4500c12280625e1f7852ce64b57bb"

client=Client(sid,auth_token)
for article in formatted_articles:
  message = client.messages.create(
  body= article,
  from_='+13854817541',
  to='+85265477959'
  )

