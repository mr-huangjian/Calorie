#!/usr/bin/python
# -*- coding: UTF-8 -*-

# chmod 777 test.py

import json, random, sys

file = open(sys.argv[1], "r")
list = json.load(file)

grammar = list["grammar"].encode("utf-8")
description = list["description"].encode("utf-8")
practices = list["practices"]

error_index = -1

def function():
	keys = practices.keys()
	random_index = random.randint(0, len(keys) - 1)

	global error_index
	if error_index != -1:
		random_index = error_index

	key = keys[random_index]
	val = practices[key]

	ch = key.encode("utf-8")
	kr = val.encode("utf-8")

	message = """
{grammar}\n{description}\n\n请翻译：{practice}\n
""".format(grammar=grammar, description=description, practice=ch)

	value = raw_input(message)

	if value.strip() == kr:
		error_index = -1
		print "您答对了! "
	else:
		error_index = random_index
		print "你答错了！\n你的答案为：_" + value + "_" + "\n正确答案为：_" + kr + "_"
	return

while 1:
		function()	

