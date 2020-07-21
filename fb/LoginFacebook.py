
'''
_FBLogin
'''
#!/usr/bin/python3
#!python*
# -*- coding: utf-8 -*-
#https://www.guru99.com/facebook-login-using-python.html
#https://stackoverflow.max-everyday.com/2019/12/selenium-chrome-options/

import os 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

################you cond######################

#客戶修改用客戶修改用客戶修改用客戶修改用客戶修改用客戶修改用客戶修改用
usernamesend_keys = "you@mail.com"
passwordsend_keys = "you@passwor"
#客戶修改用END客戶修改用END客戶修改用END客戶修改用END客戶修改用END客戶修改用END


options = webdriver.ChromeOptions() 
#禁用瀏覽器彈窗
prefs = {
     'profile.default_content_setting_values' :  {  
         'notifications' : 2  
      }  
 }  
options.add_experimental_option('prefs',prefs)

# Step 1) Open Firefox 
browser = webdriver.Chrome('../.exe/chromedriver' ,chrome_options=options)
browser.set_window_size(480, 320)

# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")

# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys(usernamesend_keys)
password.send_keys(passwordsend_keys)

# Step 4) Click Login
submit.click()

##############you cond END####################
'''
_FBLoginEND
'''
os.system("python ./1SelePage.py")
