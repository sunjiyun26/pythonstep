#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import cPickle as  pickle

d = dict(name="sunjiyun", age="31")
pickle.dumps(d)
filewrite = open("pickle.txt", mode='wb')
pickle.dump(d, filewrite)
filewrite.close()

fread = open("pickle.txt", mode="rb")
d = pickle.load(fread)
print d
fread.close()
