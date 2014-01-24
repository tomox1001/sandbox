#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
from pymongo import Connection

def extract(activity) :
    for record in activity.find({"type":"quest.complete", "content.code":"quest_event_fruitshop_chance_002"}):
        content = record["content"]
        result = True
        for drop in content["drops"] :
            # 対象コードをdropしていたらskip
            if drop["code"] == "material_fruit_mango_fruitshop_rare_1307" :
                result = False
        if result :
            # 対象アメーバIDを出力
            amebaId = record["amebaId"]
            print amebaId

# コネクション
con = Connection('10.200.0.6', 27017)
#con = Connection('10.200.0.6', 27018)
#con = Connection('10.200.0.6', 27019)
db = con["island_prd_log"]

# 抽出処理
#extract(db.Activity201307070000)
#extract(db.Activity201307070100)
#extract(db.Activity201307070200)
#extract(db.Activity201307070300)
#extract(db.Activity201307070400)
#extract(db.Activity201307070500)
#extract(db.Activity201307070600)
#extract(db.Activity201307070700)
#extract(db.Activity201307070800)
#extract(db.Activity201307070900)
#extract(db.Activity201307071000)
#extract(db.Activity201307071100)
#extract(db.Activity201307071200)
#extract(db.Activity201307071300)
#extract(db.Activity201307071400)
#extract(db.Activity201307071500)
#extract(db.Activity201307071600)
#extract(db.Activity201307071700)
extract(db.Activity201307071800)
extract(db.Activity201307071900)
extract(db.Activity201307072000)
extract(db.Activity201307072100)
extract(db.Activity201307072200)
extract(db.Activity201307072300)
