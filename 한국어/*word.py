#!/usr/bin/python
# -*- coding: UTF-8 -*-

# chmod 777 test.py

import json, random

file = open("./2019-01-27-2.json", "r")
list = json.load(file)

# list = {
# 	"排骨": "갈비",
# 	"五花肉": "삼겹살",
# 	"泡菜汤": "김치찌개",
# 	"大酱汤": "된장찌개",
# 	"嫩豆腐汤": "순두부찌개"
# }

list_keys = list.keys()
random_index = random.randint(0, len(list_keys) - 1)

key = list_keys[random_index]
val = list[key]

ch = key.encode("utf-8")
kr = val.encode("utf-8")

value = raw_input("请输入 [{}] 的韩文：\n".format(ch))

if value.strip() == kr:
	print "您答对了! "
else:
	print "你答错了！\n你的答案为：_" + value + "_" + "\n正确答案为：_" + kr + "_"


