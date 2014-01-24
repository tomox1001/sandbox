#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
from pymongo import Connection

'''
CSVファイル読み込み
'''
def readCsv():
    with open('user.csv', 'rb') as f:
    #with open('test.csv', 'rb') as f:
        reader = csv.reader(f)
        amebaIdList = []
        for row in reader:
            amebaIdList.append(row[0])
        return amebaIdList

'''
対象ユーザーを抽出する
'''
def extractTargetUser(amebaIdList):
    #url ="localhost:27017" 
    #url ="172.28.218.121:37017" 
    url ="10.200.16.101:27017" 

    con = Connection(url)
    #db = con["life_stg_main"]
    db1 = con["life_prd_main_G1"]
    db2 = con["life_prd_main_G2"]

    for amebaId in amebaIdList:
        for user in db1.User.find({'amebaId':amebaId}):
            userId = user['_id']
        exists = False;
        for ppoint in db2.CommonUserPpointRecovery.find({'_id':userId}):
            exists = True;

        if exists:
            print amebaId
            db2.CommonUserPpointRecovery.update({'_id' : userId }, {"$set" : {"quest_0430_navelorange_main_01" : { "actCounts" : [ 1 ], "data" : [ "" ], "recoveryTimes" : [ 1367473329000 ] }}})
        else:
            print amebaId
            db2.CommonUserPpointRecovery.insert({'_id' : userId , "quest_0430_navelorange_main_01" : { "actCounts" : [ 1 ], "data" : [ "" ], "recoveryTimes" : [ 1367473329000 ]}})

amebaIdList = readCsv()
extractTargetUser(amebaIdList)
