#!/usr/bin/python
# -*- coding: UTF-8 -*-

# chmod 777 test.py

import json, random, sys

file = open(sys.argv[1], "r")
list = json.load(file)

grammar = list["grammar"].encode("utf-8")
description = list["description"].encode("utf-8")
practices = list["practices"]

keys = practices.keys()
index = random.randint(0, len(keys) - 1)

key = keys[index]
val = practices[key]

ch = key.encode("utf-8")
kr = val.encode("utf-8")

message = """
{grammar}\n{description}\n\n请翻译：{practice}\n
""".format(grammar=grammar, description=description, practice=ch)

value = raw_input(message)

if value.strip() == kr:
	print "您答对了! "
else:
	print "你答错了！\n你的答案为：_" + value + "_" + "\n正确答案为：_" + kr + "_"


