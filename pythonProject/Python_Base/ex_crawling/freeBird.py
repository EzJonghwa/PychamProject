from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import csv
# 1. 브랜드별 링크를 수집
# 2. 브랜드별 링크를 수집해서 접근을 하고 내용들을 가져오기 페이징
# 3.
guitar_url = "https://www.freebud.co.kr/shop/goods/guitar_main.php?&category=026005"
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(guitar_url)
time.sleep(1)

soup = BeautifulSoup(driver.page_source,'html.parser')
div = soup.select_one('.best_brand1')
lis = div.find_all('li')
arr = []
for li in lis:
    try:
        brand = li.select_one('.txt a').text[2:]
        br_link = li.select_one('.txt a')['href'][1:]
        print(brand)
        print(br_link)
        arr.append([brand,br_link])
    except Exception as e:
        print(str(e))
with open("./data/freeBird.csv", 'a', encoding="utf-8", newline='') as f:
    write = csv.writer(f,delimiter="|")
    write.writerows(arr)
driver.quit()


