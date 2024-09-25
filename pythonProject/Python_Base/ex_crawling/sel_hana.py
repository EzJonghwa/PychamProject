from xml.etree.ElementPath import xpath_tokenizer

from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

url="https://www.hanatour.com/package/international"
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(1)
# input_keyword
# btn_search
input_search = driver.find_element(By.ID,'input_keyword')
input_search.send_keys("하와이")
driver.find_element(By.CSS_SELECTOR, 'button.btn_search').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="contents"]/div[3]/div[2]/div[1]/a').click()
time.sleep(1)
soup = BeautifulSoup(driver.page_source,'html.parser')
div = soup.select_one('.list')
lis = div.find_all('li')
for li in lis:
    try:
        title = li.select_one('.tit').text
        price = li.select_one('.price strong').text
        print("="*100)
        print("제목:"+title,"금액:"+price)
    except Exception as e:
        print(str(e))
driver.quit()




