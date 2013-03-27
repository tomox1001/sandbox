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
対象ユーザーを抽出する
'''
def extractTargetUser(amebaIdList):
	url ="localhost:27017" 
	#url ="172.28.8.151:27017" 

	con = Connection(url)

	db = con["life_dev_main"]
	userQuest = db.UserQuest

	skipCount = 0
	for record in userQuest.find():
		userId = record['_id']
		for user in db.User.find({'_id':userId}):
			 amebaId = user['amebaId']

		isSkip = False
		# チュートリアルクエストが進行中のユーザーはスキップ
		if amebaId in amebaIdList:
			for field in record["current"]:
				if field.find("tutorial") != -1:
					isSkip = True
					break
		# CSVファイルに存在しないユーザーはスキップ
		else:
			isSkip = True

		if isSkip:
			skipCount += 1
		else:
			# 対象アメーバIDを出力
			print amebaId

	print 'TotalCount:' + str(userQuest.count() - skipCount)
	print 'SkipCount:' + str(skipCount)

amebaIdList = readCsv()
extractTargetUser(amebaIdList)
