#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
netype = ['MSC','bsc']
print netype
print "netype length len(netype) is ",len(netype)
print u"第一个元素是 netype[0]",netype[0]
print u"第二个元素是 netype[1]",netype[1]
print u"索引长度超过  len(netype) 会报错 netype[2] IndexError: list index out of range \n",

print ' >'*10
print("add element to list  with method netype.append()")
netype.append("sunjiyun")
print  netype

print("\n ")
print(">>>"*10)
print("delete the lasted element to list  with method netype.pop()")
netype.pop()
print  netype


print("\n ")
print(">>>"*10)
print("delete the lasted element to list  with method netype.pop() and parameter i netype.pop(0) ")
netype.pop(0)
print  netype