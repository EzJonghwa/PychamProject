from xml.etree.ElementPath import xpath_tokenizer


from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.devtools.v85.input_ import insert_text

url="https://www.hanatour.com/package/international"
# 백그라운드에서 실행 되도록
option = webdriver.ChromeOptions()
option.add_argument('--headless=old')



def fn_search():
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    time.sleep(1)
    # input_keyword
    # btn_search
    input_search = driver.find_element(By.ID,'input_keyword')
    input_search.send_keys(entry.get())
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
            txt.insert(END,title +":"+ price + "\n")
        except Exception as e:
            print(str(e))
from tkinter import *
app =Tk()
app.title('tour search')
entry = Entry(app,width=100)
entry.pack()
btn = Button(app,text='search', command=fn_search)
btn.pack()
txt = Text(app,width=100,height=50)
txt.pack()
app.mainloop()






window.scrollTo(0,document.body.scrollHeight);