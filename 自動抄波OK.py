#!/usr/bin/python3
#!python*
# -*- coding: utf-8 -*-

import time
import datetime
import json
from pprint import pprint

import os
import sys
from urllib.request import urlopen

#客戶修改用客戶修改用客戶修改用客戶修改用客戶修改用客戶修改用客戶修改用
channel_list = ["621" , "622" , "623" , "624" , "638" , "639" , "632" , "633" , "634" , "635" , "643" , "642" , "644" , "645" , "670"]#台如有任一
DataURL = "../date/今日直播.txt"
#客戶修改用END客戶修改用END客戶修改用END客戶修改用END客戶修改用END客戶修改用END

today = datetime.date.today()
dayOfDM = str(today)[5:7]
dayOfDM1 = str(today)[8:11]
tomorrow = today + datetime.timedelta(days = 1)
dayOfWeek = datetime.date.today().weekday()
if dayOfWeek == 1: 
    dayOfWk = '星期一'
if dayOfWeek == 2: 
    dayOfWk = '星期二'
if dayOfWeek == 3: 
    dayOfWk = '星期三'
if dayOfWeek == 4: 
    dayOfWk = '星期四'
if dayOfWeek == 5: 
    dayOfWk = '星期五'
if dayOfWeek == 6: 
    dayOfWk = '星期六'
if dayOfWeek == 7: 
    dayOfWk = '星期日'

day_list = [str(today),str(tomorrow)]


u = urlopen('https://bet.hkjc.com/football/getJSON.aspx?jsontype=odds_had.aspx')#hkcj到api網
sampleDict = json.loads(u.read().decode('utf-8'))


fp = open( DataURL , "a", encoding="utf-8" )	
fp.writelines('\n今日直播'+' '+str(dayOfDM1+'/'+dayOfDM+' '+dayOfWk))


#驗
TotalNumberOfGames =  len(sampleDict[1]['matches'])#取總場數
count = 0 #=場號
while (count < TotalNumberOfGames): #場號=總場數=停
	if( 'channel' in sampleDict[1]['matches'][count]): #如有台檔
		for channel000000_ in channel_list:#台如岩
			if channel000000_ in sampleDict[1]['matches'][count]['channel'][0]['channelID']:
				for day000_list in day_list:#日如岩
					if day000_list in (sampleDict[1]['matches'][count]['matchTime']):


 

          				#取料
						matchTime = (sampleDict[1]['matches'][count]['matchTime'])
						matchTime111111 = matchTime[11:16]
						homeTeam = (sampleDict[1]['matches'][count]['homeTeam']['teamNameCH'])
						awayTeam = (sampleDict[1]['matches'][count]['awayTeam']['teamNameCH'])
						channelID = (sampleDict[1]['matches'][count]['channel'][0]['channelID'])
						fp.writelines(str( matchTime111111 + homeTeam + 'VS' + awayTeam))
						print (dayOfDM1,'/',dayOfDM,dayOfWk,matchTime111111, homeTeam,'VS',awayTeam,channelID)
						

	count += 1

	time.sleep(1)
	print ('-------------')


fp.writelines('             ')
#关闭文件
fp.close()

print ('己記錄 今日直播')

 





