import csv
import requests
from bs4 import BeautifulSoup
import re

url ="https://www.freebud.co.kr/shop/goods"
with open("./data/freeBird.csv", "r", encoding="UTF-8") as f:
    reader = csv.reader(f,delimiter="|")
    data = list(reader)
    arr =[]

for row in data:
    ele_url = url+row[1]
    res = requests.get(ele_url)
    title = re.sub(r'[^a-zA-Z0-9가-힣\s]', '', row[0])
    soup = BeautifulSoup(res.content,"html.parser")
    div = soup.select_one(".sale_king")
    tds = div.find_all("td")


    with open("./data/" + title +".csv", 'a' , encoding="UTF-8", newline='') as f:
        for td in tds:
            ele_name = td.select_one("dt")
            arr.append([ele_name])

        write = csv.writer(f,delimiter="|")
        write.writerows(arr)
        arr = []