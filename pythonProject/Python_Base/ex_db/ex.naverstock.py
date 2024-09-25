import requests

for i in range(1,46):
    url =f"https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page={i}&pageSize=50"
    res = requests.get(url)
    if res.status_code ==200:
        data= res.json()
        arr = data['stocks']
        for v in arr:
    #itemCode, stockName, closePrice
            print (v['itemCode']
                  ,v['stockName']
                  ,v['closePrice'].replace(',',''))