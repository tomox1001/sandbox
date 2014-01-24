#!/usr/bin/python
# -*- coding:utf-8 -*-

import re
import csv
from pymongo import Connection

def output(activity):
    for record in activity.find({"type":"quest.complete"}):
        content = record["content"]
        code = content["code"]
        r = re.compile('daily*')

        # ディリークエストチェック
        if r.match(code) is not None :
            drops = content["drops"]
            isOutput = True
            for drop in drops:
                if 'code' in drop:
                    # 4月チケットをドロップしていたら出力対象に含めない
                    dropcode = drop['code']
                    if dropcode == 'material_ticket_monthly_1304' :
                        isOutput = False

            if isOutput:
                amebaId = record["amebaId"]
                # 対象アメーバIDを出力
                print amebaId

con = Connection('10.200.16.6', 27017)
#con = Connection('10.200.16.6', 27018)

db = con["life_prd_log"]
activity1 = db.Activity201303270500
activity2 = db.Activity201303270600
activity3 = db.Activity201303270700
activity4 = db.Activity201303270800
activity5 = db.Activity201303270900

output(activity1)
output(activity2)
output(activity3)
output(activity4)
output(activity5)
