#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
from collections import defaultdict, OrderedDict

mydefaultDict = defaultdict(lambda: 'sunjiyun')
mydefaultDict["age"] = 31
mydefaultDict["name"] = "sunjiyun2"
print mydefaultDict['age']
print mydefaultDict['name']
print mydefaultDict.keys()

d = dict([("a", 1), ("b", 2), ("c", 3)])
print d

orderDict = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
print orderDict

orderDict["a"] =4
print  orderDict

orderDict["z"] = "z1"
orderDict["y"] = "y1"
orderDict["x"] = "x1"
print orderDict
print "OrderedDict的Key会按照插入的顺序排列，不是Key本身排序："


class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self.capacity = capacity
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey > self.capacity:
            last = self.popitem(last=False)
        if containsKey:
            del  self[key]
