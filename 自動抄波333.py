#!/usr/bin/python3
#!python*
# -*- coding: utf-8 -*-

import time
from datetime import datetime
import os
import sys
from urllib.request import urlopen
import json
from pprint import pprint
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

dayOfDM = (time.strftime("%d/%m"))
dayOfWeek = datetime.now().isoweekday()
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


u = urlopen('https://bet.hkjc.com/football/getJSON.aspx?jsontype=odds_had.aspx')#hkcj到api網
sampleDict = json.loads(u.read().decode('utf-8'))

TotalNumberOfGames =  len(sampleDict[1]['matches'])#取總場數
count = 0 #=場號

channel_list = ["621" , "622" , "623" , "624" , "638" , "639" , "632" , "633" , "634" , "635" , "643" , "642" , "644" , "645" , "670"]#台如有任一

while (count < TotalNumberOfGames): #場號=總場數=停
	if( 'channel' in sampleDict[1]['matches'][count]): #如有台

		for channel_ in channel_list:
			if channel_ in sampleDict[1]['matches'][count]['channel'][0]['channelID']:

				matchTime = (sampleDict[1]['matches'][count]['matchTime'])
				homeTeam = (sampleDict[1]['matches'][count]['homeTeam']['teamNameCH'])
				awayTeam = (sampleDict[1]['matches'][count]['awayTeam']['teamNameCH'])
				channelID = (sampleDict[1]['matches'][count]['channel'][0]['channelID'])
				print (matchTime, homeTeam,'VS',awayTeam,channelID)
	count += 1
	print ('------------------')
	time.sleep(1)
else:
	print ('Loop 死死死死.')
print ("死")


 





