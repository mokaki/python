
'''
_FBTool
#202008042151
github.com/mokaki
---
https://www.guru99.com/facebook-login-using-python.html
https://stackoverflow.max-everyday.com/2019/12/selenium-chrome-options/
显式等待 https://www.cnblogs.com/poloyy/p/12587729.html
selenium get h2 text https://zhuanlan.zhihu.com/p/132772856
https://groups.google.com/forum/#!topic/python-cn/Got2obfNZho


'''
#!/usr/bin/python3
#!python*
# -*- coding: utf-8 -*-


#global#global#global#global#global#global#global#global#global#global#global
import os
import json
import time
import requests
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import *
import tkinter as tk
from functools import partial
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

tkWindow2 = tk.Tk()
tkWindow2.geometry('1x1')     # 设置窗口的大小
L1 = Label(tkWindow2, text='facebook帳號email')   # 创建用户名输入框
name_entry = tk.Entry(tkWindow2)  
L2 = Label(tkWindow2, text='facebook密碼email')
pwd_entry = tk.Entry(tkWindow2, show='🐳')  # 创建密码输入框
#L3 = Label(tkWindow2, text='IG帳號email')
#IGname_entry = tk.Entry(tkWindow2)
#L10 = Label(tkWindow2, text='IG密碼email')
#IGpwd_entry = tk.Entry(tkWindow2, show='🐳')
L4 = Label(tkWindow2, text='帖文字內容')
txt_entry = tk.Text(tkWindow2, height=14)
L9 = Label(tkWindow2,text='存檔位置,如..\\date\\')
dateurl = tk.Entry(tkWindow2)  
options = webdriver.ChromeOptions() 
#禁用瀏覽器彈窗
prefs = {'profile.default_content_setting_values':{'notifications' : 2}}  
options.add_experimental_option('prefs',prefs)
# Step 1) Open Firefox 
browser = webdriver.Chrome('../.exe/chromedriver' ,chrome_options=options)
browser.set_window_size(480, 600)

WebDriverWaitMSG = "\n!!!找不到這個網頁原素!!!\n"
FBcode000 = str('https://www.facebook.com/')
FBcode001 = str('//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div')
FBcode002 = str('//*[@id="mount_0_0"]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div/div/div/span')
FBcode003 = str('//*[@id="mount_0_0"]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[3]/div[2]/div')
FBcode004 = str('//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div/div[1]/div[2]/span')
FBcode005 = str('//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[4]/div[2]/div/div/span')#分群
FBcode006 = str('//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div/div/div/span/h1')
FBcode007 = str('//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[5]')#分頁
FBcode008 = str('//*[@id="jsc_c_2d"]/div[1]/div/div/div/div[2]/div/div/')
#FBcode000 = str('')












#OK202008012245
#_FBLogin#_FBLogin#_FBLogin#_FBLogin#_FBLogin#_FBLogin#_FBLogin#_FBLogin#_FBLogin
def _FBLogin():
	print ('\nrun _FBLogin')
	# Step 2) Navigate to Facebook
	# ===显式等待===
	# 设置元素等待实例，最多等10秒，每0.5秒查看条件是否成立
	# 条件：直到元素加载完成
	browser.get(FBcode000)
	element = WebDriverWait(browser, 10, 0.5).until(
		EC.presence_of_element_located((By.ID, "email")),WebDriverWaitMSG + "email"
	)
	# Step 3) Search & Enter the Email or Phone field & Enter Password
	username = browser.find_element_by_id("email")
	password = browser.find_element_by_id("pass")
	submit   = browser.find_element_by_id("loginbutton")
	username.send_keys(name_entry)
	password.send_keys(pwd_entry)
	# Step 4) Click Login
	submit.click()
	time.sleep(random.uniform(3, 11))
	#取AC名
	browser.get(FBcode000+'me/')
	time.sleep(random.uniform(3, 11))
	element = WebDriverWait(browser, 10, 0.5).until(
			EC.presence_of_element_located((By.XPATH,FBcode006)),WebDriverWaitMSG + FBcode006
		)
	FBACName = browser.find_element_by_xpath(FBcode006)
	print ('\n',FBACName.text,'成功登入facebook!!')


#OK202008012245
#_FBPostMyWall#_FBPostMyWall#_FBPostMyWall#_FBPostMyWall#_FBPostMyWall#_FBPostMyWall
def _FBPostMyWall():
	print ('\nrun _FBPostMyWall')
	#是否已登入
	browser.get(FBcode000+'me/')
	time.sleep(random.uniform(3, 11))
	get_url = browser.current_url
	if get_url != FBcode000:
		#點留言
		submit2 = browser.find_element_by_xpath(FBcode001)
		submit2.click()
		#寫留言
		element = WebDriverWait(browser, 10, 0.5).until(
			EC.presence_of_element_located((By.XPATH,FBcode002)),WebDriverWaitMSG + FBcode002
		)
		_inputPost = browser.find_element_by_xpath(FBcode002)
		_inputPost.send_keys(txt_entry)
		#暫未可發圖T_T202008011755
		os.system("pause")
		sys.exit()
		#發留言
		submit3 = browser.find_element_by_xpath(FBcode003)
		submit3.click()
	else:
		#print ("您未登入")
		_SeeDate(),_FBLogin(),_FBPostMyWall()


#OK202008012245
#_FBPostGroups#_FBPostGroups#_FBPostGroups#_FBPostGroups#_FBPostGroups#_FBPostGroups
def _FBPostGroups():
	print ('\nrun _FBPostGroups')
	#是否已登入
	browser.get(FBcode000+'me/')
	time.sleep(random.uniform(3, 11))
	get_url = browser.current_url
	if get_url != FBcode000:
		slePostWhere = int(input('5=群,7=專頁'))
		#點分享 #自己wall第一帖
		element = WebDriverWait(browser, 10, 0.5).until(
			EC.presence_of_element_located((By.XPATH,FBcode004)),WebDriverWaitMSG + FBcode004
		)
		submit8 = browser.find_element_by_xpath(FBcode004)
		submit8.click()
		time.sleep(random.uniform(3, 11))
		if slePostWhere == 5:
			#點分享群
			element = WebDriverWait(browser, 10, 0.5).until(
				EC.presence_of_element_located((By.XPATH,FBcode005)),WebDriverWaitMSG + FBcode005
			)
			submit8 = browser.find_element_by_xpath(FBcode005)
			submit8.click()
		if slePostWhere == 7:
			element = WebDriverWait(browser, 10, 0.5).until(
				EC.presence_of_element_located((By.XPATH,FBcode007)),WebDriverWaitMSG + FBcode007
			)
			submit8 = browser.find_element_by_xpath(FBcode007)
			submit8.click()
		else:
			print ("手動操作")
	else:
		#print ("您未登入")
		_SeeDate(),_FBLogin(),_FBPostGroups()

















#OK202008012245
#DateFun#DateFun#DateFun#DateFun#DateFun#DateFun#DateFun#DateFun#DateFun#DateFun#DateFun#DateFun#DateFun#DateFun
def _SeeDate():
	print ('\nrun _SeeDate')
	global name_entry
	global pwd_entry
	global IGname_entry
	global IGpwd_entry
	global txt_entry
	global dateurl

	a0json = '0.json'
	if os.path.isfile(a0json):#如0檔在
		with open(a0json, 'r', encoding="utf-8") as ha0ha:
			data = json.load(ha0ha)
			name_entry = data['FBacDate'][0]['FB帳號']
			pwd_entry = data['FBacDate'][0]['FB密碼']
			IGname_entry = data['FBacDate'][0]['IG帳號']
			IGpwd_entry = data['FBacDate'][0]['IG密碼']
			txt_entry = data['FBacDate'][0]['內容']
			dateurl = 0
	else:	
		name_entry0 = input('帳號文件名')
		pwd_entry0  = input('密碼')
		dateurl0 = input('存檔位置,如..\\date\\')

		DataURL = str(dateurl0)+str(name_entry0)+'.json'
		_SeeMyDate = (str(DataURL))

		if not os.path.isfile(_SeeMyDate):#如檔不在
			print ("帳號文件不存在")
			time.sleep(5)
			sys.exit()
		else:
			with open(_SeeMyDate, 'r', encoding="utf-8") as f00123456:
				data = json.load(f00123456)
				pwd_entry = data['FBacDate'][0]['FB密碼']
				if (pwd_entry) != (pwd_entry0):#如密錯
						print ("帳號或密碼錯誤")
						time.sleep(5)
						sys.exit()
				else:
					name_entry = data['FBacDate'][0]['FB帳號']
					pwd_entry = data['FBacDate'][0]['FB密碼']
					IGname_entry = data['FBacDate'][0]['IG帳號']
					IGpwd_entry = data['FBacDate'][0]['IG密碼']
					txt_entry = data['FBacDate'][0]['內容']
					dateurl = dateurl0



def _look():
	print ("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	print ("\nFB帳號: ",name_entry)
	print ("\nFB密碼: ",pwd_entry)
	print ("\nIG帳號: ",IGname_entry)
	print ("\nIG密碼: ",IGpwd_entry)
	print ("\n內容: \n",txt_entry)
	print ("\n存檔位置: ",dateurl)
	print ("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")




def _ChangeDate():
	print ('\nrun _ChangeDate')
	tkWindow2.title('創新帳號')     # 设置窗口的标题
	tkWindow2.geometry('300x370')     # 设置窗口的大小
	L1.pack(padx=(0),pady=(0))
	name_entry.pack(padx=(0),pady=(0),ipadx=(60))
	L2.pack(padx=(0),pady=(0))
	pwd_entry.pack(padx=(0),pady=(0),ipadx=(60))

	#L3.pack(padx=(0),pady=(0))
	#IGname_entry.pack(padx=(0),pady=(0),ipadx=(60))
	#L10.pack(padx=(0),pady=(0))
	#IGpwd_entry.pack(padx=(0),pady=(0),ipadx=(60))

	L4.pack(padx=(0),pady=(0))
	txt_entry.pack(padx=(7),pady=(5))
	#SaveDate
	button = tk.Button(tkWindow2,
		text='開始',                      # 显示在按钮上的文字
		bg='green',
		command=_SaveDate)                  # 点击按钮时执行的函数
	button.pack(fill=X,pady=(10,10),ipady=(20)) # 将按钮锁定在窗口上
	L9.pack(padx=(0),pady=(0))
	dateurl.pack(padx=(0,0),pady=(0),ipadx=(60))
	tkWindow2.mainloop()       # 启动窗口

def _SaveDate():
	print ('\nrun _SaveDate')
	informations = {
		'FBacDate': [
			{
				'FB帳號': name_entry.get(),
				'FB密碼': pwd_entry.get(),
				'IG帳號': IGname_entry.get(),
				'IG密碼': IGpwd_entry.get(),
				'內容': txt_entry.get(1.0, END)
			}
		]
	}
	path = dateurl.get()+name_entry.get()[0:7]+"_"+time.strftime('%Y%m%d%H%M%S')+'.json'
	json_str = json.dumps(informations, ensure_ascii=False, indent=4) # 缩进4字符
	with open(path, 'w', encoding="utf-8") as json_file:
		json_file.write(json_str)
	print ('已保存\n'+str(informations))
	tkWindow2.destroy()

























#OK202008012245
#功能表#功能表#功能表#功能表#功能表#功能表#功能表#功能表#功能表#功能表#功能表#功能表#功能表
tkWindow = Tk()  
tkWindow.geometry('300x300')  
tkWindow.title('FBTool 請選擇功能 ')



L0241 = Label(tkWindow, text='將資料保存為 0.json \n並存放在程式同一位置\n即可自動執行該帳號')   #
L0241.pack(padx=(0),pady=(0))



#_ChangeDate
ChangeDateButton = Button(tkWindow,text='記錄', command=_ChangeDate).pack(fill=X,ipady=(10))
#_FBLogin
_FBLoginButton = Button(tkWindow,text='登入Facebook', command=lambda:[_SeeDate(),_FBLogin()]).pack(fill=X,ipady=(10))
#_FBPostMyWall
_FBPostMyWallButtonButton = Button(tkWindow,text='Facebook發帖', command=_FBPostMyWall).pack(fill=X,ipady=(10))
#_FBPostGroups
lFBPostGroupsButtonButton = Button(tkWindow,text='Facebook群分享', command=_FBPostGroups).pack(fill=X,ipady=(10))
#_IGPost
#_IGPostButton = Button(tkWindow,text='_IG發帖').pack(fill=X,ipady=(10))
#_lookDate
SeeDateButton = Button(tkWindow,text='查看記錄', command=lambda:[_SeeDate(),_look()]).pack(fill=X,ipady=(10))

tkWindow.mainloop()
