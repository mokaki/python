
'''
py3
Get Rar Catalog
202106222047
pip install threaded

使用線程重複功能
http://tw.gitbook.net/t/python3/article-83.html
必须是end=' \r'
http://www.21fanqie.com/thread-162-1-1.html
此代碼段具有令人讨厌的功能，每个數字都print在換行符上.為避免這種情况，您可以
https://t.codebug.vip/questions-2848742.htm
'''



#!/usr/bin/env python
from threading import *
import time
import os
from PyClassicRound import classic_round



for i in range(600):
	print(round(((i)/60),1),'分鐘',"\r离程序退出还剩%s秒" % (1+i), end="")
	time.sleep(1)



print('按鍵退出程式')
os.system("pause")