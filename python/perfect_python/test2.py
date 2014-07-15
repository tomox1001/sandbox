#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = 10

def exe2():
    print("exe2 start %d" % x)
    for i in range(1, 6):
        if i % 2 == 0:
            print("%sは偶数です" % i)
        else:
            print("%sは奇数です" % i)
