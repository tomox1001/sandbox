#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
from pymongo import Connection

'''
CSVファイル読み込み
'''
def readCsv():
    #with open('test.csv', 'rb') as f:
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
    #url1 ="172.28.218.180:37017" 
    #url2 ="172.28.218.180:37018" 
    url1 ="10.200.0.5:27017" 
    url2 ="10.200.0.5:27018" 

    con1 = Connection(url1)
    con2 = Connection(url2)
    #db1 = con1["island_stg_main"]
    #db2 = con2["island_stg_main"]
    db1 = con1["island_prd_main"]
    db2 = con2["island_prd_main"]

    for amebaId in amebaIdList:
        print amebaId
        for user in db1.User.find({'amebaId':amebaId}):
            userCode = user['_id']
            db2.UserPoint.update({ "_id" : userCode }, { "$inc" : { "coin" : 50 } })

amebaIdList = readCsv()
extractTargetUser(amebaIdList)
