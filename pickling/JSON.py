#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'

import json

d = dict(name="sunjiyun",age="25")
str  = json.dumps(d)

file = open("json.txt","wb")
json.dump(d,file)
file.close()

file = open("json.txt",'rb')
str = file.readline()
print  json.loads(str)
file.close()

