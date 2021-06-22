

'''
py3
PythonUnzipRARImage
202106221856
pip install os

pip install rarfile
https://stackoverflow.com/questions/64121660/how-to-unpack-rar-file-in-python
pip install Pillow
http://hk.uwenku.com/question/p-ubupikwp-ke.html
'''



import rarfile
import os
import io
from PIL import Image








d4 = "html/assets/images/banner2.jpg"

rf = rarfile.RarFile("18345.rar")
for f in rf.infolist():
	print(f.filename, f.file_size)
	
	if f.filename == d4:
		print('\n``````````````````````````````````\n')
		img_png = Image.open(io.BytesIO(rf.read(f))) 
		img_png.save('mg.jpg')
		print(rf.read(f))
		print('\n``````````````````````````````````\n')


print ('\n己完成記錄 今日直播\n請按任意鍵退出')
os.system("pause")



