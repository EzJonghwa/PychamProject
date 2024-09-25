import csv
from os import write

import requests
from bs4 import BeautifulSoup
import urllib.request as req
import os
import re

#image download

# req.urlretrieve('https://image.cine21.com/resize/cine21/poster/2024/0826/10_43_11__66cbddaf49c14[F230,329].jpg','test.jpg')

url = "http://m.cine21.com/movie/boxoffice/history"
res = requests.get(url)
soup = BeautifulSoup(res.content,"html.parser")
div = soup.select_one('.lst_ranking_area')
lis = div.find_all('li')
arr = []

for li in lis:
    detail_url = li.select_one('.title a')['href']
    title = li.select_one('.title a').text
    score = li.select_one('.sub_info').text
    rating = li.select_one('.num').text
    print(detail_url,title,score,rating)
    print('='*60)
    arr.append([title, score, rating, detail_url])
print(arr)

with open("./data/movie.csv", 'a', encoding="utf-8", newline='') as f:
    write = csv.writer(f,delimiter="|")
    write.writerows(arr)

# rows = 배열을 여러개로 저장 하겠다 / row = 한 배열에 다 집어넣음

# # 상세정보 url
# detail = soup.select_one('.title a')['href']
# print(detail)

# # 영화제목
# title = soup.select_one('.title a').text
# print(title)

# # 관객수
# score = soup.select_one('.sub_info')
# print(score.text)
# # 평점 정보
# rating = soup.select_one('.num')
# print(rating.text)
#


# print('='*60)
#
#
# print(detail,title,score,rating)
