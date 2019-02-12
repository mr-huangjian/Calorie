#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, random, sys, io
import getRandomIndex

filePath = './word.json'

# 获取原数据
file = io.open(filePath, "r")
list = json.load(file)
file.close()

# 产生随机数
index = getRandomIndex.getRandomIndex()

# 获取该键值对
item = list[index]
zh = item["zh"].encode("utf-8")
kr = item["kr"].encode("utf-8")
weight = item["weight"]

# 提示用户输入，并判断正误
input = raw_input("请输入 [{}] 的韩文：\n".format(zh))
new_item = {
	"zh": zh.decode("utf-8"),
	"kr": kr.decode("utf-8")
}

if input.strip() == kr:
	# 正确则增加权重+1
	new_item["weight"] = weight + 1
	print "您答对了! \n"
else:
	# 错误则减少权重-2
	new_item["weight"] = weight - 2
	print "你答错了！\n你的答案为：_" + input + "_" + "\n正确答案为：_" + kr + "_\n"

list[index] = new_item
file = io.open(filePath, 'w')
text = json.dumps(list, ensure_ascii=False, sort_keys=True, indent=2, separators=(',', ': '))
file.write(text)
file.close()
