
#蛇料88db
#202009160149
#!/usr/bin/python3
#!python*
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os 
import json
import time
import datetime
import random
from tkinter import *
import tkinter as tk
from functools import partial
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re  



BCR			= "../.exe/chromedriver"							#ChromedriverURL
WeMSG		= "\n********!!!找不到這個網頁原素!!!********\n"		#ERROR MSG
WeMSGEND	= "\n****************"



#88db網code
URL000 = 'https://88db.com.hk/Business/'
URL001 = 'Business-for-Sale/1/'						#生意頂讓
URL002 = 'Accounting-Tax/1/'						#會計及稅務
URL003 = 'Renovation/1/'							#裝修工程
URL004 = 'Interior-Design/1/'						#室內設計
URL005 = 'Building-Construction/1/'					#建築及建造
URL006 = 'Stock-Yard/1/'							#存貨場地
URL007 = 'Logistics-Storage/1/'						#物流及倉儲
URL008 = 'Cargo-Factory-Container-Yard/1/'			#貨廠及貨櫃場
URL009 = 'Heavy-Transport/1/'						#重型運輸
URL010 = 'Courier-Service/1/'						#速遞
URL011 = 'Environmental-Engineering-Recycling/1/'	#環保設備及回收
URL012 = 'Business-Start-Up-Aliance/1/'				#創業加盟
URL013 = 'Marketing-Communications/1/'				#市場策劃
URL014 = 'Event-Meeting-Venue-Rental/1/'			#會議/展覽場地出租
URL015 = 'Pop-up-Store/1/'							#展銷場
URL016 = 'Exhibition-Event-Management/1/'			#展覽會及活動策劃
URL017 = 'Printing-Publishing/1/'					#印刷
URL018 = 'Stationery-Gifts/1/'						#文儀及精品
URL019 = 'Office-Furniture-Fittings/1/'				#辦公室傢俬及設備
URL020 = 'Private-Investigator/1/'					#私家偵探
URL021 = 'Copywriting/1/'							#撰稿
URL022 = 'Translate/1/'								#翻譯
URL023 = 'Legal/1/'									#法律事務
URL024 = 'Consulting/1/'							#顧問
URL025 = 'Lesson-Instruction/1/'					#教學進修
URL026 = 'Raw-Materials-and-Products/1/'			#原料及製品
URL027 = 'Cleaning-Pest-Control/1/'					#清潔及滅蟲
URL028 = 'Investment-Immigration-working-visa/1/'	#投資移民及簽證
URL029 = 'Loan/1/'									#貸款
URL030 = 'Finance-Investment/1/'					#金融投資及保險
URL031 = 'Fire-Equipment/1/'						#消防
URL032 = 'Special-Offer/1/'							#商業優惠
URL033 = 'Security-Services/1/'						#保安服務
URL034 = 'Event-Activity/1/'						#節目及活動
URL035 = 'Club-Association/1/'						#會社、組織及團體
URL036 = 'Recruitment/1/'							#業內招聘
URL037 = '3D-Print/1/'								#3D立體打印
URL038 = 'BBA-MBA-Courses/1/'						#商管課程
URL039 = 'Statistic-Courses/1/'						#統計課程
URL040 = 'Professional-Courses/1/'					#語言課程
URL041 = 'Professional-Courses/1/'					#專業課程
URL042 = 'Self-Improve-Courses/1/'					#個人提升課程
URL043 = 'Startup-Courses/1/'						#創業課程

co1		= str('//*[@id="listing-filter-1"]/div[3]/div[2]/span[1]') #總數


co2		= str('//*[@id="grid"]/div/div[1]/div[2]/div[2]/div[*]/div[1]/div/a')
co3		= str('//*[@id="grid"]/div/div[1]/div[2]/div[3]/div[*]/div[1]/div/a')
co4		= str('//*[@id="grid"]/div/div[1]/div[2]/div[4]/div[*]/div[1]/div/a')
co5		= str('//*[@id="grid"]/div/div[1]/div[2]/div[5]/div[*]/div[1]/div/a')
co6		= str('')
co7		= str('')
co8		= str('')
co9		= str('')
c10		= str('')
c11		= str('')
c12		= str('')
c13		= str('')
c14		= str('')
c15		= str('')
c16		= str('')
c17		= str('')
c18		= str('')
c19		= str('')
c20		= str('')
c21		= str('//*[@id="grid"]/div/div[1]/div[2]/div[21]/div[*]/div[1]/div/a')



def _see88dbData():#_see88dbData#_see88dbData#_see88dbData#_see88dbData#_see88dbData#_see88dbData
	#瀏覽器
	options = webdriver.ChromeOptions() 										
	prefs   = {'profile.default_content_setting_values':{'notifications' : 2}}		#禁用瀏覽器彈窗
	options.add_experimental_option('prefs',prefs)
	options.add_argument('--headless')												#冇頭
	options.add_argument('--no-sandbox')											#冇頭
	options.add_argument("--log-level=3")											#不提示log
	browser = webdriver.Chrome(BCR ,chrome_options=options)
	#browser.set_window_size(480, 600)											
	#瀏覽器END



	#到網+初始資料
	browser.get(URL000+URL001)	
	element = WebDriverWait(browser, 10, 0.5).until(					#co8作錨點 沒co8會報錯
			EC.presence_of_element_located((By.XPATH,co2)),WeMSG + co2 + WeMSGEND
		)

	
	d02 = browser.find_elements_by_xpath(co2) 
	d02url = d02[0].get_attribute("href")

	d03 = browser.find_elements_by_xpath(co3) 
	d03url = d03[0].get_attribute("href")

	d04 = browser.find_elements_by_xpath(co4) 
	d04url = d04[0].get_attribute("href")

	d05 = browser.find_elements_by_xpath(co5) 
	d05url = d05[0].get_attribute("href")

	d21 = browser.find_elements_by_xpath(c21) 
	d21url = d21[0].get_attribute("href")


	print(d02url,'**************\n')
	print(d03url,'**************\n')
	print(d04url,'**************\n')
	print(d05url,'**************\n')
	print(d21url,'**************\n')


	os.system("pause")




_see88dbData()
