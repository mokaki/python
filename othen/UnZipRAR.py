
# https://tw.clearwatergardenclub.org/985574-how-to-read-a-text-YZVZWS


import rarfile
import os

DataURL = "ind1ex.html"
fp = open( DataURL , "a", encoding="utf-8" )	

with rarfile.RarFile("18333.rar") as rf:
	with rf.open("html/index.html") as f:
		for ln in f:
			

			ewqqew1 = ln.strip()
			ewqqew1 = ewqqew1.decode("utf-8")
			ewqqew1 = ewqqew1.replace('><', '>\n<') 
			print (ewqqew1)
			fp.writelines(ewqqew1)

fp.close()


print ('\n己完成記錄 今日直播\n請按任意鍵退出')
os.system("pause")


