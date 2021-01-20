'''
win10操作jons文件功能
202101202244
github/mokaki
'''
#!/usr/bin/python3
#!python*





import os
import json
import time




#############################################_MakeDate
def _MakeDate():
	print ('\n創新文件 _MakeDate 202101202244')
	Jonsinput0 = input('''
		*******自動整網系統 歡迎您*******\n
		請依次輸入\n
		存檔名>存檔內容1>存檔內容2\n
		謝謝\n
		*******************************\n\n
請輸入存檔名...''')
	Jonsinput1 = input('存檔內容1...')
	Jonsinput2 = input('存檔內容2...')
	print ('開始存檔')
	JonsinputAll = {
		'Date': [
			{
			#############################################
				'存檔名': Jonsinput0,
				'存檔內容1': Jonsinput1,
				'存檔內容2': Jonsinput2
			#############################################
			}
		]
	}
	path = Jonsinput0+"_"+time.strftime('%Y%m%d%H%M%S')+'.json'
	json_str = json.dumps(JonsinputAll, ensure_ascii=False, indent=4) # 缩进4字符
	with open(path, 'w', encoding="utf-8") as json_file:
		json_file.write(json_str)
	print ('已保存\n'+str(JonsinputAll))
	_SeeDate()
#############################################_MakeJonsEND




#############################################_SeeDate
def _SeeDate():
	print ('\n查文件 _SeeDate 202101202244')
	a0json = '0.json'
	if os.path.isfile(a0json):					#如0檔在
		with open(a0json, 'r', encoding="utf-8") as ha0ha:
			data = json.load(ha0ha)
			Jonsinput0 = data['Date'][0]['存檔名']
			Jonsinput1 = data['Date'][0]['存檔內容1']
			Jonsinput2 = data['Date'][0]['存檔內容2']
			print ("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
			print ("\n存檔名 ",Jonsinput0)
			print ("\n存檔內容1 ",Jonsinput1)
			print ("\n存檔內容2 ",Jonsinput2)
			print ("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
			os.system("pause")
	else:									#0檔不在入名
		print ('\n您可以將文件命名為 0.json 即可自動執行')
		Jonsinput0 = input('請輸入存檔名')
		dateurl0 = input('存檔位置,如..\\date\\*可沒有')
		DataURL = str(dateurl0)+str(Jonsinput0)+'.json'
		_SeeMyDate = (str(DataURL))

		if not os.path.isfile(_SeeMyDate):	#入名檔都不在
			print ("帳號文件不存在\n轉去創新文件")
			_MakeDate()
		else:
			with open(_SeeMyDate, 'r', encoding="utf-8") as ha1ha:
				data = json.load(ha1ha)
				Jonsinput0 = data['Date'][0]['存檔名']
				Jonsinput1 = data['Date'][0]['存檔內容1']
				Jonsinput2 = data['Date'][0]['存檔內容2']
				print ("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
				print ("\n存檔名 ",Jonsinput0)
				print ("\n存檔內容1 ",Jonsinput1)
				print ("\n存檔內容2 ",Jonsinput2)
				print ("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
				os.system("pause")


#############################################_SeeDateEND

_SeeDate()