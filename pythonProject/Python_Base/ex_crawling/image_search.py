from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from os import makedirs, mkdir
import urllib.request as req
from bs4 import BeautifulSoup


option = webdriver.ChromeOptions()
option.add_argument('--headless=old')

def fn_search():
    url = f"https://www.google.com/search?q={entry.get()}"
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a/div').click()
    cur_h =driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script(f'window.scrollTo(0,{cur_h});')
        time.sleep(1)
        n_h = driver.execute_script('return document.body.scrollHeight')

        if cur_h == n_h:
            break;
        cur_h=n_h
    body = driver.find_element(By.TAG_NAME, 'body')
    imgs = body.find_elements(By.TAG_NAME, 'img')
    img_set = set()
    for img in imgs:
        if img.get_attribute('src') != None:
            img_set.add(img.get_attribute('src'))
    print(img_set)
    driver.close()
    root = "./"
    img_dir = os.path.join(root,entry.get())

    if not os.path.exists(img_dir):
        os, mkdir(img_dir)

    for i, v in enumerate(img_set):
        file_path = os.path.join(img_dir, str(i) + '.png')
        try:

            req.urlretrieve(v, file_path)

        except Exception as e:
            print(str(e))


from tkinter import *
app =Tk()
app.title('search')
label=Label(app,text='검색어')
label.pack()
entry = Entry(app,width=30)
entry.pack()
btn = Button(app,text='수집',command=fn_search)
btn.pack()
txt = Text(app,width=50,height=25)
txt.pack()
app.mainloop()