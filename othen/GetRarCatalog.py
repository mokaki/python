
'''
py3
Get Rar Catalog
202106221759

pip install os
pip install rarfile
https://stackoverflow.com/questions/64121660/how-to-unpack-rar-file-in-python

'''


import rarfile
import os


#("./18345.rar")
#("html/assets/images/banner2.jpg")

rf = rarfile.RarFile("18345.rar")
for f in rf.infolist():
    print(f.filename, f.file_size)
    if f.filename == "README":
        print(rf.read(f))


print ('\n己完成記錄 今日直播\n請按任意鍵退出')
os.system("pause")


