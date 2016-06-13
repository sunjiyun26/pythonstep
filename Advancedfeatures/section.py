#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
print '切片'
_list = range(0,100,1)

r = []
n = 3
for i in range(n):
    r.append(_list[i])
    print r
print('1:3',_list[1:3])
print(_list[-9:])
print 'range(0,100):',range(1,99,2)
print _list[:2]
print _list[:10]
print _list[-20:-10]
print(_list[10:20])
print(_list[::5])

print(">>>>>"*10)
print("tuple")

print((1,2,3,4,5,6,7,8,9)[:3])

print(">>>>>"*10)
print("string")

print('abcdefghijk'[:3])
