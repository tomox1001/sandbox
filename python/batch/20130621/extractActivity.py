#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
from pymongo import Connection

#con = Connection('10.200.0.6', 27017)
#con = Connection('10.200.0.6', 27018)
con = Connection('10.200.0.6', 27019)

db = con["island_prd_log"]
activity = db.Activity201306211100

for record in activity.find({"type":"freight.help", "time":{ "$gt": 1371781740000, "$lt": 1371782280000}}):
    amebaId = record["amebaId"]
    # 対象アメーバIDを出力
    print amebaId
