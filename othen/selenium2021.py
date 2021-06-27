﻿

'''
202106270908

selenium2021

pip install selenium

https://www.learncodewithmike.com/2020/05/python-selenium-scraper.html

https://sites.google.com/a/chromium.org/chromedriver/downloads
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
 
 
options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://www.facebook.com/")
 
email = chrome.find_element_by_id("email")
password = chrome.find_element_by_id("pass")
 
email.send_keys('example@gmail.com')
password.send_keys('*****')
password.submit()