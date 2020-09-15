#2SelePage.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os 
from tkinter import *
from functools import partial



name = input('招財酒吧管理系統 歡迎您')
name000000 = "python "
name011111 = "./"
name022222 = ".py"
name033333 = ((name011111 + name + name022222))

def 自動發廣告():
	os.system("python ./自動發廣告.py")
	return

def 自動抄波():
	os.system("python ./自動抄波.py")
	return

def 自動播歌():
	os.system("python ./自動播歌.py")
	return

def aaaaaa1111111111():
	os.system((name000000 + name033333))
	return



#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('招財酒吧管理系統 請選擇功能 ')

#自動發廣告
loginButton = Button(tkWindow, text="自動發廣告", command=自動發廣告).grid(row=1, column=1)  

#自動抄波
loginButton2 = Button(tkWindow, text="自動抄波", command=自動抄波).grid(row=2, column=2)  

#自動播歌
loginButton3 = Button(tkWindow, text="自動播歌", command=自動播歌).grid(row=3, column=3)  

#自定義
loginButton4 = Button(tkWindow, text=str(name), command=aaaaaa1111111111).grid(row=9, column=9)  

tkWindow.mainloop()

os.system("pause")
