#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, random, sys, io

"""
新增单词
1. Python 文件读写
    http://www.runoob.com/python/file-methods.html
    https://blog.csdn.net/weixin_42737442/article/details/82027328
"""

file = io.open('../word.json', 'r+')
list = json.load(file)

zh = raw_input("请输入中文：")
kr = raw_input("请输入韩文：")
print "您输入的单词是：[{}] - [{}]\n".format(zh, kr)

if raw_input("确认插入？").strip() == "":
    new_item = {
        "zh": zh.decode("utf-8"),
        "kr": kr.decode("utf-8"),
        "weight": -8
    }
    list.append(new_item)

    text = json.dumps(list, ensure_ascii=False, sort_keys=True, indent=2, separators=(',', ': '))
    file.seek(0)
    file.truncate()
    file.write(text)
    print "插入成功！"

file.close()
