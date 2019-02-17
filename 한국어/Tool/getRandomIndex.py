#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, random, numpy as np

"""
根据权重以某个概率随机生成索引
1. Python 没有三目运算符
2. Python 设置函数默认值
    http://baijiahao.baidu.com/s?id=1602330535408996217&wfr=spider&for=pc
    https://www.cnblogs.com/crazyrunning/p/6867849.html
3. Python json.load/json.loads/json.dump/json.dumps 区别与字符编码
    https://www.cnblogs.com/shiju/p/9511916.html
    https://www.cnblogs.com/biangbiang/archive/2013/02/19/2916780.html
    https://www.jianshu.com/p/345c79ac5826
    https://www.cnblogs.com/xiaomingzaixian/p/7286793.html
    https://www.cnblogs.com/wswang/p/5411826.html
4. Python 字符串的编码与解码
    https://www.cnblogs.com/linjiqin/p/3674825.html
    https://www.cnblogs.com/Xjng/p/3809781.html
    https://blog.csdn.net/m0_38080253/article/details/78841280
5. Python 深度学习
    https://www.coursera.org/specializations/deep-learning
6. Python 随机概率
    https://blog.csdn.net/qq_20011607/article/details/82288561
    https://blog.csdn.net/vicdd/article/details/52667709
    https://blog.csdn.net/Cryhelyxx/article/details/72822234
    https://blog.csdn.net/zn505119020/article/details/78190993
"""

didRememberAllWords = False

def getRandomIndex(topP=0.00, baseP=0.20, lowP=0.80):
    global didRememberAllWords

    filePath = './word.json'

    file = open(filePath, "r")
    list = json.load(file)
    file.close()

    if len(list) == 0:
        exit()

    baseMaxLevel = 4
    baseMinLevel = -3

    topList = []
    lowList = []
    baseList = []

    for index in range(0, len(list)):
        item = list[index]
        weight = item["weight"]

        if 8 > weight > baseMaxLevel:
            topList.append(index)
        elif baseMinLevel <= weight <= baseMaxLevel:
            baseList.append(index)
        elif weight < baseMinLevel:
            lowList.append(index)

    if didRememberAllWords == False and len(lowList) == 0 and len(baseList) == 0 and len(topList) > 0:
        didRememberAllWords = True
        print "真棒，你已全部记住了！\n"

    level = np.random.choice([1, 0, -1], p=[topP, baseP, lowP])

    if level == 1:
        if len(topList) == 0:
            return getRandomIndex()
        return topList[random.randrange(0, len(topList))]
    elif level == 0:
        if len(baseList) == 0:
            return getRandomIndex()
        return baseList[random.randrange(0, len(baseList))]
    elif level == -1:
        if len(lowList) == 0:
            return getRandomIndex()
        return lowList[random.randrange(0, len(lowList))]
