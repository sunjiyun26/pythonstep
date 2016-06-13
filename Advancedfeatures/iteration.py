#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
from collections import Iterable
print '迭代用 for  in'
_dict ={"name":'sunjiyun','age':31}
for i in _dict:
    print "key is ",i,">>>>>>>> value is _dict[i]",_dict[i]
print ''
for k,v in _dict.items():
    print  k,">>>>>>>>>",v
print '''默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.itervalues()，
    如果要同时迭代key和value，可以用for k, v in d.iteritems()。'''
for ch in 'abcdefg':
    print ch

print  '如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：'
print 'isinstance(\'abc\',Iterable)',isinstance('abc',Iterable)
print 'isinstance([1,2,3],Iterable)',isinstance([1,2,3],Iterable)
print "isinstance(123,Iterable)",isinstance(123,Iterable)

for i, value in enumerate(['A', 'B', 'C']):
    print i ,value

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x,y