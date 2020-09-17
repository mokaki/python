
#蛇料88db建築及建造
#202009180408
#!/usr/bin/python3
#!python*
# -*- coding: utf-8 -*-
import os 
import time
import random
from selenium import webdriver



BCR			= "../.exe/chromedriver"							#ChromedriverURL
WeMSG		= "\n********!!!找不到這個網頁原素!!!********\n"		#ERROR MSG
WeMSGEND	= "\n****************"
DL01		= "Data/"
DL02		= ".txt"

#88db網code
URL000 = 'https://88db.com.hk/Business/'
URL001 = 'Building-Construction/1/'					#建築及建造


#列表頁總數
co1	   = str('//*[@id="listing-filter-1"]/div[3]/div[2]/span[1]') 
#列表頁的每產品的圖的href
co2	   = str('//*[@id="grid"]/div/div[1]/div[2]/div[')
co2B   = str(']/div[*]/div[1]/div/a')

#產品頁的TEL
co3	= str('//*[@id="norDetails"]/div[4]/div[1]/div/div/div[3]/div[*]/div[*]/a[*]')			#WTS
co4	= str('//*[@id="norDetails"]/div[4]/div[1]/div/div/div[3]/div[*]/div[2]/div/div[*]/a')	#TEL
co5	= str('//a[text()="後頁"]')																#後頁

#瀏覽器
options = webdriver.ChromeOptions() 										
prefs   = {'profile.default_content_setting_values':{'notifications' : 2}}		#禁用瀏覽器彈窗
options.add_experimental_option('prefs',prefs)
options.add_argument('--headless')												#冇頭
options.add_argument('--no-sandbox')											#冇頭
options.add_argument("--log-level=3")											#不提示log
browser = webdriver.Chrome(BCR ,chrome_options=options)
#browser.set_window_size(640, 360)					
#瀏覽器END

#初始資料
browser.get(URL000+URL001)										#到網
DL00 = str(DL01+'88dbDate-建築及建造'+time.strftime('%Y%m')+DL02)				#文件名	88dbDate-202009.txt
fp = open(DL00, "a", encoding="utf-8" )							#開/創文件
fp.writelines('88dbDate-建築及建造'+time.strftime('%H%M%S')+'\n')			#文件第一行
fp.close()






#找資
def _see88dbData():#_see88dbData#_see88dbData#_see88dbData#_see88dbData#_see88dbData#_see88dbData
	count = 2													#列表頁內的數 2~21
	#列表頁內找21次
	while (count <= 21):  										#少於21執行
		co2000  = str(co2 + str(count) + co2B)					#正式列表頁的每產品的圖
		d02 = browser.find_elements_by_xpath(co2000)
		if d02 != []:											#列表頁有該號產品
			d02url = d02[0].get_attribute("href")				#取圖的href
			browser.get(d02url)									#入href取聯
			time.sleep(random.uniform(3, 11))					#隨機等
			d03 = (browser.find_elements_by_xpath(co3))			#找WTS
			d04 = (browser.find_elements_by_xpath(co4))			#冇WTS找TEL
			while True:
				if d03 == [] and d04 == []:								#冇WTS冇TEL走
					print ("\n冇WTS冇TEL走")
					break
				else:
					d03WTS = d03[0].get_attribute("href")				#找WTSURL
					while True:
						if d03WTS != None :		#WTS非空
							#time.sleep(random.uniform(3, 11))			#隨機等
							d03WTS = d03[0].get_attribute("href")
							fp = open(DL00, "a", encoding="utf-8" )	
							fp.writelines((d03WTS[36:47])+'\n')			#記WTS
							fp.close()
							print ("\n成功取得建築及建造WTS聯絡資料",(d03WTS[36:47]))
							break
						else:			
							d04 = (browser.find_elements_by_xpath(co4))	#冇WTS找TEL
							while True:
								if d04 != []:							#TEL非空
									#time.sleep(random.uniform(3, 11))	#隨機等
									fp = open(DL00, "a", encoding="utf-8" )	
									fp.writelines((d04[0].text)+'\n')	#記TEL
									fp.close()
									print ("\n成功取得建築及建造TEL聯絡資料",(d04[0].text))
									break
								else:									#冇TEL下個
									break
							break										#記完退
				break
			browser.back()										#回列表頁
			count += 1											#列表頁內的數+1
		else:													#冇產品回
			print ("\n冇產品或不夠20個")
			count = 21
			break
	#列表頁內找21次END
	_changePagea()







#轉下頁至冇後頁
SortBy = 0
def _changePagea():#_changePagea#_changePagea#_changePagea#_changePagea#_changePagea
	global SortBy
	time.sleep(random.uniform(3, 11))								#隨機等
	d05 = (browser.find_elements_by_xpath(co5))						#後頁btn
	if d05 == [] :	
		print ("\n已成功取得所有頁的聯絡資料了")						#冇後頁OUT
		print ("\n下個類")
	else:
		if d05[0].text == '後頁' :									#夠21,轉後頁
			browser.execute_script("arguments[0].click();", d05[0]) #特別點擊
			SortBy += 20
			SortBy2 = SortBy + 20
			print('\n***建築及建造' , SortBy , '至' , SortBy2  ,'*****************\n')
			_see88dbData()
	fp = open(DL00, "a", encoding="utf-8" )
	fp.writelines('完'+time.strftime('%H%M%S')+"\n")					#文件尾行
	fp.close()
	print ("\nEND")
	os.system("pause")




_see88dbData()






