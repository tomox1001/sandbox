#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
from pymongo import Connection

def extract(activity) :
    for record in activity.find({"type":"gift.get", "time":{ "$gt": 1375167620000, "$lt": 1375171218000}}):
        # 対象アメーバIDを出力
        amebaId = record["amebaId"]
        rewards = record["content"]["rewards"]

        print amebaId
        print rewards

        for reward in rewards:
            type = reward["type"]
            itemtype = reward["itemtype"]
            code = reward["code"]
            value = reward["value"]

            #print amebaId + ',' + type + ',' + itemtype + ',' + code + ',' + str(value)

# コネクション
#con = Connection('10.200.0.6', 27017)
#con = Connection('10.200.0.6', 27018)
con = Connection('10.200.0.6', 27019)
db = con["island_prd_log"]

# 抽出処理
extract(db.Activity201307301600)
extract(db.Activity201307301700)
