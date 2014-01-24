#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
from pymongo import Connection

#con = Connection('10.200.0.6', 27017)
#con = Connection('10.200.0.6', 27018)
con = Connection('10.200.0.6', 27019)

db = con["island_prd_log"]
activity = db.Activity201306010000

for record in activity.find({"type":"item.instant.decreaseItem", "content.code":"instant_booster_plant_event_ajisai_1306"}):
    amebaId = record["amebaId"]
    # 対象アメーバIDを出力
    print amebaId
