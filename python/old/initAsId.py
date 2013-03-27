#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
from pymongo import Connection

'''
CSVファイル読み込み
'''
def readCsv():
	with open('user.csv', 'rb') as f:
		reader = csv.reader(f)
		amebaIdList = []
		for row in reader:
			amebaIdList.append(row[0])
		return amebaIdList

'''
対象ユーザーのデカ情報を初期化する
'''
def init(amebaIdList):
	url ="localhost:27017" 
	#url ="172.28.8.151:27017" 

	con = Connection(url)

	db = con["life_prd_main"]
	user = db.User

	for amebaId in amebaIdList:
		user.update({'amebaId':amebaId}, {'$unset':{'asId':1}});

amebaIdList = readCsv()
init(amebaIdList)
