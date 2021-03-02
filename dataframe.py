import pyupbit
import requests
import pandas as pd
from bs4 import BeautifulSoup

result = []
days=29

for day in range(days):
    if day ==0:
        continue
    for hour in range(24):
        
            if day < 10:
                date="2021-03-0"+str(day)
            else:    
                date="2021-03-"+str(day)
            
            if hour < 10:
                time = "0"+str(hour)+":00:00"
            else:
                time = str(hour)+":00:00"

            url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/1?code=CRIX.UPBIT.KRW-MOC&count=60&to='+date+"%20"+time
            req = requests.get(f'{url}')
            data = req.json()
            print(url)
            for i,candle in enumerate(data):
                result.append({
                'Time' : data[i]["candleDateTimeKst"],
                'open' : data[i]["openingPrice"],
                'high' : data[i]["highPrice"],
                'low' : data[i]["lowPrice"],
                'trade' : data[i]["tradePrice"],
                'tradevol' : data[i]["candleAccTradeVolume"],
                'traceprice' : data[i]["candleAccTradePrice"]
                })

            coindata=pd.DataFrame(result)
            coindata.to_csv(f'{date}-{time}.csv')
            result=[]