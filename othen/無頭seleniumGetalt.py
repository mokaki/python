# -*- coding: utf-8 -*-
#!/usr/bin/python3


#今天星期月日
import time
from datetime import datetime
import os

#今天星期月日END


import sys


from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


#chrome_options = 無頭
chrome_options = Options() # 啟動無頭模式
chrome_options.add_argument('--headless')  #規避google bug
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome('../.exe/chromedriver',chrome_options=chrome_options)
#browser.set_window_size(480, 320)
browser.get("https://bet.hkjc.com/football/index.aspx")
xpath_urls = browser.find_element_by_xpath('//*[@id="secMenuHR"]').get_attribute("title")

print(str(xpath_urls))



