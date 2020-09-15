
#勞聯資
#20200915080218
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

#基本
DL01			= "../date/" 																		#您的存檔位
DL02			= "勞聯資.json"
chromedriverURL	= "../.exe/chromedriver"

WeMSG			= "\n******************!!!找不到這個網頁原素!!!******************\n"
WeMSGEND		= "\n***********************************************************"
today			= datetime.date.today()
dayOfe			= str(today)[0:4] 																	#今年號
dayOfm			= str(int(str(today)[5:7]))															#今月號/0
dayOfd			= str(today)[8:11]																	#今日號
ss1textnum002	= 1																					#JS第一行初始

#努網code
url01	= 'https://www1.jobs.gov.hk/1/0/WebForm/jobseeker/jobsearch/quickview.aspx?SearchFor=vac_by_date&ID='
url02	= str('&SortBy=&from=&start=')
url03	= str('//*[@id="uxResult"]/tbody/tr[')														#左邊格 點20次
url04	= str(']')
co0		= str('//*[@id="ctl00_ContentPlaceHolder1_uxTotalPage"]/span[1]')							#空缺數

co1		= str('//*[@id="ctl00_ContentPlaceHolder1_uxJobCard_uxJcard"]/table[2]/tbody/tr[1]/td[1]')	#編號
co2		= str('//*[@id="ctl00_ContentPlaceHolder1_uxJobCard_uxJcard"]/table[2]/tbody/tr[1]/td[2]')	#日期
co3		= str('//*[@id="ctl00_ContentPlaceHolder1_uxJobCard_uxJobTitleDiv"]')						#職位
co4		= str('//*[@id="ctl00_ContentPlaceHolder1_uxJobCard_uxJcard"]/table[2]/tbody/tr[3]/td')		#公司/僱主名稱
co5		= str('//*[@id="ctl00_ContentPlaceHolder1_uxJobCard_uxJcard"]/table[2]/tbody/tr[4]/td[1]')	#地區
co6		= str('//*[@id="ctl00_ContentPlaceHolder1_uxJobCard_uxJcard"]/table[2]/tbody/tr[4]/td[2]')	#行業
co7		= str('//*[@id="ctl00_ContentPlaceHolder1_uxJobCard_uxJcard"]/table[2]/tbody/tr[5]/td')		#職責資歷待遇
co8		= str('//*[@id="ctl00_ContentPlaceHolder1_uxJobCard_uxJcard"]/table[2]/tbody/tr[6]/td')		#申請須知
co9		= str('//*[@id="ctl00_ContentPlaceHolder1_uxJobCard_uxJcard"]/table[2]/tbody/tr[7]/td')		#備註















def _seeToDay():#_seeToDay#_seeToDay#_seeToDay#_seeToDay#_seeToDay#_seeToDay#_seeToDay#_seeToDay
	global ss1textnum002
	#瀏覽器
	options = webdriver.ChromeOptions() 										
	prefs   = {'profile.default_content_setting_values':{'notifications' : 2}} 					#禁用瀏覽器彈窗
	options.add_experimental_option('prefs',prefs)
	options.add_argument('--headless')															#冇頭
	options.add_argument('--no-sandbox')														#冇頭
	options.add_argument("--log-level=3")														#不提示log
	browser = webdriver.Chrome(chromedriverURL ,chrome_options=options)
	#browser.set_window_size(480, 600)											
	#瀏覽器END



	#使用者input日期,沒=今日
	name = input('\n現在是'+time.strftime('%Y年%m月%d日-%H:%M:%S')+'\n請問您需要獲得本月那一天資料\n*不需0,限本月')
	if name == '':
		allurl = str(url01 + dayOfd + '/' + dayOfm + '/' + dayOfe)
	else:
		allurl = str(url01 + name + '/' + dayOfm + '/' + dayOfe)



	#到網+初始資料
	browser.get(allurl)																			#打開app,網址+日期自動
	allurl10 = allurl[-10:] 																	#allurl10aaa=只日期數字
	allurl10aaa = re.sub(u"([^\u0030-\u0039])","",allurl10)					
	ss0 = (browser.find_element_by_xpath(co0)).text												#空缺數



	#使用者input日期,空缺=0 空缺!=0
	if int(ss0) == 0:																			#空缺=吉
		print('\n*****************',allurl10aaa,'暫時沒有資料*****************\n')
		os.system("pause"),_selLOex()
	else:
		DL00 = str(DL01+(allurl10aaa.replace('/', ''))+'-'+time.strftime('%Y%m%d%H%M%S')+DL02)	#文件名
		informations001 = {'資料日期':allurl10aaa,'總數':ss0,'開始時間':time.strftime('%H%M%S')}		#日:總 #第一行字
		json_st01r = json.dumps(informations001, ensure_ascii=False, indent=4)					#缩进4字符
		with open(DL00, 'a', encoding="utf-8") as json_file:									#開文件寫入第一行字
			json_file.write(json_st01r)
		print('\n**************',allurl10aaa,'共有',ss0,'個資料**************\n')



		#每一頁動作
		SortBy = 0																	 #初始頁定位 一頁20工,下頁+20
		while (int(ss0) != 0):											 			 #click20次後轉頁=allurl+20=allurlN20
			count = 1



			#click20次搜尋結果排序 1~20
			while (count <= 20): 
				element = WebDriverWait(browser, 10, 0.5).until(					#co8作錨點 沒co8會報錯
						EC.presence_of_element_located((By.XPATH,co8)),WeMSG + co8 + WeMSGEND
					)
				d01 = browser.find_element_by_xpath(co1).text						#編號
				d02 = browser.find_element_by_xpath(co2).text						#日期
				d03 = browser.find_element_by_xpath(co3).text						#職位
				d04 = browser.find_element_by_xpath(co4).text						#公司/僱主名稱
				d05 = browser.find_element_by_xpath(co5).text						#地區
				d06 = browser.find_element_by_xpath(co6).text						#行業
				d07 = browser.find_element_by_xpath(co7).text						#職責資歷待遇
				d08 = browser.find_element_by_xpath(co8).text						#申請須知=聯資
				d09 = browser.find_element_by_xpath(co9).text						##備註


				#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資
				print(d02,'\n',d03,'\n',d05,'\n',d07,'\n',d08,'\n****************************',ss1textnum002,'/',ss0,'***\n')

	
	
				# 加到J尾
				with open(DL00, encoding="utf-8") as f31010102:
					dat2a = json.load(f31010102)
					dat2a[str(ss1textnum002)] = str(d01),str(d02),str(d03),str(d04),str(d05),str(d06),str(d07),str(d08),str(d09)
				os.remove(DL00)
				with open(DL00, 'a', encoding="utf-8") as f31010102:
					json.dump(dat2a, f31010102, ensure_ascii=False, indent=4)
				# 加到J尾END


				#click20次下個
				count += 1
				count00 = str(count)
				allc9 = str(url03 + count00 + url04)							#搜尋結果下一個
				ss1 = browser.find_element_by_xpath(allc9)
				ss1textnum = ss1.text[0:4]									#現點工號純數	
				ss1textnum002 = ss1textnum.split()[0]						#空格後不要
				#ss1textnum002 = re.sub(u"([^\u0030-\u0039])","",ss1textnum)

				if ss1textnum002 == ss0:									#現點工號=空缺數=回
					break
				else:
					ss1.click()												#現點工號!=空缺數=點
				if (count == 20): 											#一頁20工,點晒回
					break
			#click20次搜尋結果排序 1~20END



			#轉頁
			SortBy += 20															#下頁+20
			SortBy2 = SortBy + 20
			print('\n*****************' ,SortBy , '至' , SortBy2 , '*****************\n')
			allurlN20 = str(allurl + url02 + str(SortBy))	  						#搜尋結果下一頁
			browser.get(allurlN20)
			ss0 = (browser.find_element_by_xpath(co0)).text							#空缺數



			#最後
			if (int(ss0) == 0): 													#到最後+20頁,空缺數=0
				print('\n成功取得',ss1textnum002,'個資料\n')
				# 加到J尾 完成
				with open(DL00, encoding="utf-8") as f31010102:
					dat2a = json.load(f31010102)
					dat2a['完成時間'] = time.strftime('%H%M%S')
				os.remove(DL00)
				with open(DL00, 'a', encoding="utf-8") as f31010102:
					json.dump(dat2a, f31010102, ensure_ascii=False, indent=4)
				# 加到J尾END
				print('\n',allurl10aaa,'-',str(time.strftime('%Y%m%d-%H%M%S')),'資料已保存\n')
				break
		#每一頁動作END
	os.system("pause"),_selLOex()

















#使用者動作
def _selLOex():
	selL001 = input('\n從新開始請按1\n或直接Enter退出')
	if str(selL001) != '':
		_seeToDay()
	else:
		quit()






_seeToDay()#打開app,網址+日期自動




