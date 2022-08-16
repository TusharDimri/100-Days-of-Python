from pydoc import describe
import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv


load_dotenv()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% (1% for me) between yesterday and the day before yesterday then print("Get News").
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

def getPercentageChange(stock):
    
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "apikey":ALPHA_VANTAGE_API_KEY,
    }

    url = "https://www.alphavantage.co/query"

    res = requests.get(url=url, params=params)

    data = res.json()["Time Series (Daily)"]
    required_data = []
    i=0

    for key, value in data.items():
        if(i<2):
            required_data.append([key, value])
            i+=1

    day1 = float(required_data[0][1]["4. close"])
    day2 = float(required_data[1][1]["4. close"])

    percentage_change = ((day2 - day1) / day2) * 100
    percentage_change = round(percentage_change, 2)
    print(f"{percentage_change}%")

    return percentage_change

percentage_change = getPercentageChange(STOCK)
if(abs(percentage_change)> 1):
    print("News Please")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def getNews(company):
    params = {
        "apikey" : NEWS_API_KEY,
        "q" : company,
        "language":"en",
    }

    url = "https://newsapi.org/v2/everything"

    res = requests.get(url=url, params=params)
    # print(res.json())
    news_data = res.json()["articles"][0]["description"]
    # for i in range(3):
    #     try:
    #         print(news_data[i]["description"])
    #     except Exception as e:
    #         print(e)
    
    return news_data


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_number = os.environ.get("TWILIO_NUMBER")
my_number = os.environ.get("MY_NUMBER")

news = getNews(COMPANY_NAME)


if percentage_change > 0:
    msg = f"{STOCK}: 🔺{percentage_change}\nHeadline:{news}"
elif percentage_change < 0:
    msg = f"{STOCK}: 🔻{percentage_change}\nHeadline:{news}"
else:
    msg = f"{STOCK}: -{percentage_change}\nHeadline:{news}"


client = Client(account_sid, auth_token)
message = client.messages \
            .create(
                    body=msg,
                    from_=twilio_number,
                    to=my_number
                )