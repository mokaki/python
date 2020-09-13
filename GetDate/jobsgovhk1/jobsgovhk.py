
#勞聯資
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
DataURL						= "../date/"
DataURL1					= "勞聯資.txt"
chromedriverURL				= "../.exe/chromedriver"

WebDriverWaitMSG			= "\n******************!!!找不到這個網頁原素!!!******************\n"
WebDriverWaitMSGEND			= "\n***********************************************************"
today						= datetime.date.today()
dayOfe						= str(today)[0:4] 				#今年號
dayOfm						= str(int(str(today)[5:7]))		#今月號/0
dayOfd						= str(today)[8:11]				#今日號

#努網code
url01	= 'https://www1.jobs.gov.hk/1/0/WebForm/jobseeker/jobsearch/quickview.aspx?SearchFor=vac_by_date&ID=' #勞網
c93		= str('&SortBy=&from=&start=')
co0		= str('//*[@id="ctl00_ContentPlaceHolder1_uxTotalPage"]/span[1]')							          #空缺數
co1		= str('//*[@id="ctl00_ContentPlaceHolder1_uxJobCard_uxAppNote"]')
c91		= str('//*[@id="uxResult"]/tbody/tr[')														   #click20次
c92		= str(']')










def _seeToDay():#_seeToDay#_seeToDay#_seeToDay#_seeToDay#_seeToDay#_seeToDay#_seeToDay#_seeToDay


	#瀏覽器
	options = webdriver.ChromeOptions() 										
	prefs   = {'profile.default_content_setting_values':{'notifications' : 2}}  #禁用瀏覽器彈窗
	options.add_experimental_option('prefs',prefs)
	options.add_argument('--headless')											#冇頭
	options.add_argument('--no-sandbox')										#冇頭
	options.add_argument("--log-level=3")										#不提示log
	browser = webdriver.Chrome(chromedriverURL ,chrome_options=options)
	#browser.set_window_size(480, 600)											
	#瀏覽器END



	#input日期,沒=今日
	name = input('\n現在是'+time.strftime('%Y年%m月%d日-%H:%M:%S')+'\n請問您需要獲得本月那一天資料\n*冇0,限本月')
	if name == '':
		allurl = str(url01 + dayOfd + '/' + dayOfm + '/' + dayOfe)
	else:
		allurl = str(url01 + name + '/' + dayOfm + '/' + dayOfe)
	browser.get(allurl)																	    #打開app,網址+日期自動
	allurl10 = allurl[-10:] 															   #allurl10aaa=只日期數字
	allurl10aaa = re.sub(u"([^\u0030-\u0039])","",allurl10)					
	ss0 = (browser.find_element_by_xpath(co0)).text#空缺數



	if int(ss0) == 0:#空缺=吉
		print('\n*****************',allurl10aaa,'暫時沒有資料*****************\n')
		os.system("pause"),_selLOex()
	else:

		DataURL00 = str(DataURL+(allurl10aaa.replace('/', ''))+'-'+time.strftime('%Y%m%d%H')+DataURL1)   # 文件名
		fp = open(DataURL00  , "a", encoding="utf-8" )													#打開文件
		fp.writelines(allurl10aaa+'-'+str(time.strftime('%Y%m%d-%H%M%S'))+'='+ss0+'\n')
		print('\n**************',allurl10aaa,'共有',ss0,'個資料**************\n')
		fp.close()																						#关闭文件

		#每一頁
		SortBy = 0																				#一頁20工,下頁+20
		while (int(ss0) != 0): 						 				    	 #click20次後轉頁=allurl+20=allurlN20
			count = 1
			#click20次搜尋結果排序 1~20
			while (count <= 20): 
				element = WebDriverWait(browser, 10, 0.5).until(		#沒co1會報錯
						EC.presence_of_element_located((By.XPATH,co1)),WebDriverWaitMSG + co1 + WebDriverWaitMSGEND
					)
				d01 = browser.find_element_by_xpath(co1).text			#申請須知=聯資
				print(d01)#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資#聯資
				fp = open(DataURL00  , "a", encoding="utf-8" )			#打開文件
				fp.writelines('\n'+str(d01))
				fp.close()												#关闭文件
				count += 1
				count00 = str(count)
				allc9 = str(c91 + count00 + c92)						#搜尋結果下一個
				ss1 = browser.find_element_by_xpath(allc9)
				ss1textnum = ss1.text[0:4]								#現點工號純數	
				ss1textnum002 = re.sub(u"([^\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",ss1textnum)
				if ss1textnum002 == ss0:								#現點工號=空缺數=回
					break
				else:
					ss1.click()
				if (count == 20): 										#一頁20工,點晒回
					break
			#click20次搜尋結果排序 1~20END

			SortBy += 20																			   #下頁+20
			SortBy2 = SortBy + 20
			print('\n*****************' ,SortBy , '至' , SortBy2 , '*****************\n')
			allurlN20 = str(allurl + c93 + str(SortBy))	  									     #搜尋結果下一頁
			browser.get(allurlN20)
			ss0 = (browser.find_element_by_xpath(co0)).text												#空缺數


			if (int(ss0) == 0): 														   #到最後+20頁,空缺數=0
				print('\n成功取得',ss1textnum002,'個資料\n')
				fp = open(DataURL00  , "a", encoding="utf-8" )										   #打開文件
				fp.writelines('\n'+allurl10aaa+'-'+str(time.strftime('%Y%m%d-%H%M%S'))+'-END')
				fp.close()																			   #关闭文件
				print('\n',allurl10aaa,'-',str(time.strftime('%Y%m%d-%H%M%S')),'資料已保存\n')

				break
		#每一頁END


	os.system("pause"),_selLOex()



def _selLOex():
	selL001 = input('\n從新開始請按1\n或直接Enter退出')


	print('\n',str(selL001))
	os.system("pause")



	if str(selL001) != '':
		_seeToDay()
	else:
		quit()



_seeToDay()#打開app,網址+日期自動


