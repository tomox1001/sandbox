#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
from pymongo import Connection

#con = Connection('10.200.16.6', 27017)
con = Connection('10.200.16.6', 27018)

db = con["life_prd_log"]
activity = db.Activity201303180800

for record in activity.find({"type":"quest.complete", "content.code":"0315_asparagus_01"}):
    amebaId = record["amebaId"]
    # 対象アメーバIDを出力
    print amebaId
