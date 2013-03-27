#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
from pymongo import Connection

'''
CSVファイル読み込み
'''
def readCsv():
    with open('user20130220.csv', 'rb') as f:
        reader = csv.reader(f)
        amebaIdList = []
        for row in reader:
            amebaIdList.append(row[0])
        return amebaIdList

'''
対象ユーザーを抽出する
'''
def extractTargetUser(amebaIdList):
    url ="10.200.16.101:27017" 
    #url ="172.28.8.151:27017" 

    con = Connection(url)

    db = con["life_prd_main_G1"]
    skipCount = 0

    for amebaId in amebaIdList:
        for user in db.User.find({'amebaId':amebaId}):
             userId = user['_id']

        for body in db.UserBody.find({'_id':userId}):
            gender = body['gender']
            if gender == 'male':
                print amebaId 

amebaIdList = readCsv()
extractTargetUser(amebaIdList)
