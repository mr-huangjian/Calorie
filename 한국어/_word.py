#!/usr/bin/python
# -*- coding: utf-8 -*-

# chmod 777 test.py

import json, random, sys, time

def getRunTime(startTime):
    endTime = time.time()
    seconds = endTime - startTime
    m, s = divmod(seconds, 60)
    return "%02d:%02d" % (m, s)

file = open(sys.argv[1], "r")
list = json.load(file)

startTime = time.time()

class MemoryWords:
	passWeight = 4
	repeatIndex = None

	def __init__(this, list):
		this.list = list
		this.listKeys = list.keys()
		this.listCount = len(list)
		this.weight = [0 for i in range(this.listCount)]

	def getRandomIndex(this):
		index = random.randint(0, this.listCount - 1)
		if this.repeatIndex != None:
			index = this.repeatIndex
		else:
			if this.weight == [this.passWeight for i in range(this.listCount)]:
				print "Well Done! 🎉 Total time {} \n".format(getRunTime(startTime))
				exit()
			elif this.weight[index] >= this.passWeight:
				return this.getRandomIndex()
		return index

	def run(this):
		while 1:
			idx = this.getRandomIndex()
			key = this.listKeys[idx]
			val = this.list[key]
			key = key.encode("utf-8")
			val = val.encode("utf-8")

			input = raw_input("请输入 [{}] 的韩文： (已花费 {})\n".format(key, getRunTime(startTime)))

			if input.strip() == val:
				this.repeatIndex = None
				this.weight[idx] = this.weight[idx] + 1
				print "您答对了! \n"
			else:
				this.repeatIndex = idx
				this.weight[idx] = this.weight[idx] - 2
				print "你答错了！\n你的答案为：_" + input + "_" + "\n正确答案为：_" + val + "_\n"


MemoryWords(list).run()
