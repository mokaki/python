
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
import sys
import os


def handleClient1():
	for i in range(10,0,-1):
		sys.stdout.write(str(i)+' \r')
		sys.stdout.flush()
		time.sleep(1)


 





handleClient1()

print('按鍵退出程式')
os.system("pause")