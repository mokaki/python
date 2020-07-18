# -*- coding: utf-8 -*-


import time
from datetime import datetime

#今天星期
dayOfWeek = datetime.now().isoweekday()
dayOfDM = (time.strftime("%d/%m"))

# 打开文件
fp = open("../../date/今qwe2日5435直播.txt", "a",encoding="utf-8")
fp.writelines('\n今日直5播 '+str(dayOfDM)+' '+str(dayOfWeek))
# 关闭文件
fp.close()
