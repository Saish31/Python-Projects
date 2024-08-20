import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY="***********"
NEWS_API_KEY="****************************"

ACCOUNT_SID="*********************************"
AUTH_TOKEN="******************************"

stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}

response=requests.get(STOCK_ENDPOINT,params=stock_params)
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yest_data=data_list[0]
yest_closing=yest_data["4. close"]
print(yest_closing)

daybefore_data=data_list[1]
daybefore_closing=daybefore_data["4. close"]
print(daybefore_closing)

diff=float(daybefore_closing)-float(yest_closing)
if diff>0:
    sign="🔺"
elif diff<0:
    sign="🔻"
print(diff)
diffperc=round((diff/float(yest_closing))*100)
print(diffperc)

if abs(diffperc)>5:
    news_params={
        "apiKey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME
    }
    news_response=requests.get(NEWS_ENDPOINT,params=news_params)
    articles=news_response.json()["articles"]
    three_articles=articles[:3]

    formatted_articles=[f"{STOCK_NAME}: {sign}{diffperc}% \nHeadline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]

    client=Client(ACCOUNT_SID,AUTH_TOKEN)

    for article in formatted_articles:
        msg=client.messages.create(
            body=article,
            from_="*********68",
            to="**********09"
        )



