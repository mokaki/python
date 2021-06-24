
'''
py3
批量讀取資料夾檔案
202106250717
pip install os

python批量讀取資料夾檔案、修改檔案
https://ithelp.ithome.com.tw/m/articles/10229795
'''



#!/usr/bin/env python
# -*- coding: UTF-8 -*-



import os
def find_dir(path):
    # 函數功能: 遞迴顯示指定路徑下的所有檔案及資料夾名稱
    for fd in os.listdir(path):
        full_path=os.path.join(path,fd)
        if os.path.isdir(full_path):
            print('資料夾:',full_path)
            find_dir(full_path)
        else:
            print('檔案:',full_path)
            
path="./" #指向當前資料夾的路徑
find_dir(path)



print('按鍵退出程式')
os.system("pause")