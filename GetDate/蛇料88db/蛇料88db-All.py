
#蛇料88db-All
#202009200611
#!/usr/bin/python3
#!python*
# -*- coding: utf-8 -*-

import os 
import time
import random
from selenium import webdriver


BCR		= "../.exe/chromedriver"				#ChromedriverURL
WeMSG		= "\n********!!!找不到這個網頁原素!!!********\n"		#ERROR MSG
WeMSGEND	= "\n****************"
DL01		= "Data/"
DL02		= ".txt"

#88db網code
URL0 = 'https://88db.com.hk/Business/'
URL1 = 'Business-for-Sale/1/'						#生意頂讓
URL2 = 'Accounting-Tax/1/'						#會計及稅務
URL3 = 'Renovation/1/'							#裝修工程
URL4 = 'Interior-Design/1/'						#室內設計
URL5 = 'Building-Construction/1/'					#建築及建造
URL6 = 'Stock-Yard/1/'							#存貨場地
URL7 = 'Logistics-Storage/1/'						#物流及倉儲
URL8 = 'Cargo-Factory-Container-Yard/1/'				#貨廠及貨櫃場
URL9 = 'Heavy-Transport/1/'						#重型運輸
URL10 = 'Courier-Service/1/'						#速遞
URL11 = 'Environmental-Engineering-Recycling/1/'			#環保設備及回收
URL12 = 'Business-Start-Up-Aliance/1/'					#創業加盟
URL13 = 'Marketing-Communications/1/'					#市場策劃
URL14 = 'Event-Meeting-Venue-Rental/1/'					#會議/展覽場地出租
URL15 = 'Pop-up-Store/1/'						#展銷場
URL16 = 'Exhibition-Event-Management/1/'				#展覽會及活動策劃
URL17 = 'Printing-Publishing/1/'					#印刷
URL18 = 'Stationery-Gifts/1/'						#文儀及精品
URL19 = 'Office-Furniture-Fittings/1/'					#辦公室傢俬及設備
URL20 = 'Private-Investigator/1/'					#私家偵探
URL21 = 'Copywriting/1/'						#撰稿
URL22 = 'Translate/1/'							#翻譯
URL23 = 'Legal/1/'							#法律事務
URL24 = 'Consulting/1/'							#顧問
URL25 = 'Lesson-Instruction/1/'						#教學進修
URL26 = 'Raw-Materials-and-Products/1/'					#原料及製品
URL27 = 'Cleaning-Pest-Control/1/'					#清潔及滅蟲
URL28 = 'Investment-Immigration-working-visa/1/'			#投資移民及簽證
URL29 = 'Loan/1/'							#貸款
URL30 = 'Finance-Investment/1/'						#金融投資及保險
URL31 = 'Fire-Equipment/1/'						#消防
URL32 = 'Special-Offer/1/'						#商業優惠
URL33 = 'Security-Services/1/'						#保安服務
URL34 = 'Event-Activity/1/'						#節目及活動
URL35 = 'Club-Association/1/'						#會社、組織及團體
URL36 = 'Recruitment/1/'						#業內招聘
URL37 = '3D-Print/1/'							#3D立體打印
URL38 = 'BBA-MBA-Courses/1/'						#商管課程
URL39 = 'Statistic-Courses/1/'						#統計課程
URL40 = 'Language-Courses/1/'						#語言課程
URL41 = 'Professional-Courses/1/'					#專業課程
URL42 = 'Self-Improve-Courses/1/'					#個人提升課程
URL43 = 'Startup-Courses/1/'						#創業課程

ClassName1  = '生意頂讓'
ClassName2  = '會計及稅務'
ClassName3  = '裝修工程'
ClassName4  = '室內設計'
ClassName5  = '建築及建造'
ClassName6  = '存貨場地'
ClassName7  = '物流及倉儲'
ClassName8  = '貨廠及貨櫃場'
ClassName9  = '重型運輸'
ClassName10 = '速遞'
ClassName11 = '環保設備及回收'
ClassName12 = '創業加盟'
ClassName13 = '市場策劃'
ClassName14 = '會議展覽場地出租'
ClassName15 = '展銷場'
ClassName16 = '展覽會及活動策劃'
ClassName17 = '印刷'
ClassName18 = '文儀及精品'
ClassName19 = '辦公室傢俬及設備'
ClassName20 = '私家偵探'
ClassName21 = '撰稿'
ClassName22 = '翻譯'
ClassName23 = '法律事務'
ClassName24 = '顧問'
ClassName25 = '教學進修'
ClassName26 = '原料及製品'
ClassName27 = '清潔及滅蟲'
ClassName28 = '投資移民及簽證'
ClassName29 = '貸款'
ClassName30 = '金融投資及保險'
ClassName31 = '消防'
ClassName32 = '商業優惠'
ClassName33 = '保安服務'
ClassName34 = '節目及活動'
ClassName35 = '會社組織及團體'
ClassName36 = '業內招聘'
ClassName37 = '3D立體打印'
ClassName38 = '商管課程'
ClassName39 = '統計課程'
ClassName40 = '語言課程'
ClassName41 = '專業課程'
ClassName42 = '個人提升課程'
ClassName43 = '創業課程'

URL000 = URL0+URL43 							#初始URL
ClassName000 = ClassName43 						#初始ClassName
classcount = 43 							#初始class號
DL00 = 0 								#初始文件名






#列表頁總數
co1	   = str('//*[@id="listing-filter-1"]/div[3]/div[2]/span[1]') 
#列表頁的每產品的圖的href
co2	   = str('//*[@id="grid"]/div/div[1]/div[2]/div[')
co2B   = str(']/div[*]/div[1]/div/a')

#產品頁的TEL
co3	= str('//*[@id="norDetails"]/div[4]/div[1]/div/div/div[3]/div[*]/div[*]/a[*]')		#WTS
co4	= str('//*[@id="norDetails"]/div[4]/div[1]/div/div/div[3]/div[*]/div[2]/div/div[*]/a')	#TEL
co5	= str('//a[text()="後頁"]')							      #後頁

#瀏覽器
options = webdriver.ChromeOptions() 										
prefs   = {'profile.default_content_setting_values':{'notifications' : 2}}		#禁用瀏覽器彈窗
options.add_experimental_option('prefs',prefs)
options.add_argument('--headless')							#冇頭
options.add_argument('--no-sandbox')							#冇頭
options.add_argument("--log-level=3")							#不提示log
browser = webdriver.Chrome(BCR ,chrome_options=options)
#browser.set_window_size(640, 360)					
#瀏覽器END




#初始資料
def _BaesData():
	global URL000
	global ClassName000
	global DL00
	print ("\n開始獲取",ClassName000,"資料")
	browser.get(URL000)															#到網
	DL00 = str(DL01 + '88dbDate-'+ ClassName000 + time.strftime('%Y%m') + DL02)	#文件名	88dbDate-創業課程202009.txt
	fp = open(DL00, "a", encoding="utf-8" )										#開/創文件
	fp.writelines('88dbDate-' + ClassName000 + time.strftime('%H%M%S') +'\n')	#文件第一行
	fp.close()
	_see88dbData()








#找資
def _see88dbData():#_see88dbData#_see88dbData#_see88dbData#_see88dbData#_see88dbData#_see88dbData
	global ClassName000
	global DL00
	count = 2												#列表頁內的數 2~21
	print ("\n正在取得",ClassName000,"資料,每頁2~21")
	#列表頁內找21次
	while (count <= 21):  											#少於21執行
		co2000  = str(co2 + str(count) + co2B)						#正式列表頁的每產品的圖
		d02 = browser.find_elements_by_xpath(co2000)
		if d02 != []:											#列表頁有該號產品
			d02url = d02[0].get_attribute("href")							#取圖的href
			browser.get(d02url)									#入href取聯
			#time.sleep(random.uniform(3, 11))							#隨機等
			d03 = (browser.find_elements_by_xpath(co3))						#找WTS
			d04 = (browser.find_elements_by_xpath(co4))						#冇WTS找TEL
			while True:
				if d03 == [] and d04 == []:							#冇WTS冇TEL走
					print ("\n冇WTS冇TEL走")
					break
				else:
					d03WTS = d03[0].get_attribute("href")					#找WTSURL
					while True:
						if d03WTS != None :		#WTS非空
							#time.sleep(random.uniform(3, 11))			#隨機等
							d03WTS = d03[0].get_attribute("href")
							fp = open(DL00, "a", encoding="utf-8" )	
							fp.writelines((d03WTS[36:47])+'\n')			#記WTS
							fp.close()
							print ("\n成功取得",ClassName000,"WTS聯絡資料",(d03WTS[36:47]))
							break
						else:			
							d04 = (browser.find_elements_by_xpath(co4))		#冇WTS找TEL
							while True:
								if d04 != []:					#TEL非空
									#time.sleep(random.uniform(3, 11))	#隨機等
									fp = open(DL00, "a", encoding="utf-8" )	
									fp.writelines((d04[0].text)+'\n')	#記TEL
									fp.close()
									print ("\n成功取得",ClassName000,"TEL聯絡資料",(d04[0].text))
									break
								else:						#冇TEL下個
									break
							break							#記完退
				break
			browser.back()										#回列表頁
			count += 1										#列表頁內的數+1
		else:												#冇產品回
			print ("\n冇產品或不夠20個")
			count = 21
			break
	#列表頁內找21次END
	_changePagea()







#轉下頁至冇後頁
SortBy = 0
def _changePagea():#_changePagea#_changePagea#_changePagea#_changePagea#_changePagea
	print ("\n轉下頁")
	global ClassName000
	global SortBy
	#time.sleep(random.uniform(3, 11))									#隨機等
	d05 = (browser.find_elements_by_xpath(co5))								#後頁btn
	if d05 == [] :	
		print ("\n已成功取得所有頁的聯絡資料了")							    #冇後頁OUT
		_changeclass()
	else:
		if d05[0].text == '後頁' :								      #夠21,轉後頁
			browser.execute_script("arguments[0].click();", d05[0]) #特別點擊
			SortBy += 20
			SortBy2 = SortBy + 20
			print('\n***', ClassName000 ,  SortBy , '至' , SortBy2  ,'*****************\n')
			_see88dbData()









#轉下個類
def _changeclass():#_changeclass#_changeclass#_changeclass#_changeclass#_changeclass
	print ("\n轉下個類")
	global classcount
	global ClassName000
	global URL000
	global DL00

	if classcount == 1:											#倒數取class = 1 = 停
		fp = open(DL00, "a", encoding="utf-8" )
		fp.writelines('完'+time.strftime('%H%M%S')+"\n")			#文件尾行
		fp.close()
		print ("\n已成功取得全網所有頁聯絡資料=END\n")
		os.system("pause")
	else:	
		classcount -= 1
		URL000 = URL0+ (eval('URL'+str(classcount)))			#URL000 = URL0+(eval內是合成的變量名稱) = URL0+URL1
		ClassName000 = (eval('ClassName'+str(classcount)))		#ClassName000 = (eval內是合成的變量名稱) = ClassName1
		print ("\n",ClassName000,URL000)
		_BaesData()



















_BaesData()



