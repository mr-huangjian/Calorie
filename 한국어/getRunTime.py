#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

"""
获取运行花费时长
https://www.jb51.net/article/118699.htm
https://www.jb51.net/article/147479.htm
"""
def getRunTime(startTime):
    endTime = time.time()
    seconds = endTime - startTime
    m, s = divmod(seconds, 60)
    return "%02d:%02d" % (m, s)
