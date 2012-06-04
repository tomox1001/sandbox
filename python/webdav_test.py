#!/usr/bin/env python
#-*- coding: utf-8 -*-

import glob

def list_files(path):
    targetPy = path+'/*.py'
    targetLog = path+'/*.log'
    return glob.glob(targetPy) + glob.glob(targetLog)

files = list_files('.')
print files
