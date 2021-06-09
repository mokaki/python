
'''
DlwProgress
ATW202106091825

pip install os
pip install requests
pip install urllib

https://home.gamer.com.tw/creationDetail.php?sn=4800729

'''
# -*- coding: UTF-8 -*-

import os
import requests
import urllib


import sys
from urllib.request import urlretrieve


htmlname1 = "18330.rar"
url = 'http://www.mobanwang.com/mb/showsoftdown.asp?urlid=1&softid=18335'


def progress(block_num, block_size, total_size):
    # block_num  : A count of blocks transferred so far
    # block_size : A block size in bytes
    # total_size : The total size of the file
    sys.stdout.write('\r下載模板 %s %.1f%%' % (htmlname1, float(block_num * block_size) / float(total_size) * 100.0))
    sys.stdout.flush()




def _DlwProgress():
    #下載模板
    print ("正在取得模板資源...")
    r = requests.get(url)
    with open(htmlname1, "wb") as code:
        code.write(r.content)
    urllib.request.urlretrieve(url, htmlname1, progress)
    print()
    print ("完成下載!!")
    os.system("pause")

        
_DlwProgress()
