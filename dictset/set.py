#!/usr/bin/env python
# -*- coding:utf-8 -*-
print 'set'
myset = set(["sunjiyun","31","jinan"])
print myset

print 'set add element with add function myset.add(1)'
myset.add(1)
print myset

print 'set delete element with remove function myset.remove(\'sunjiyun\')'
myset.remove("sunjiyun")
print myset

print ">"*20
print "取交集 set 的方法是 用 & 符号  s1 * s2,set 保留相同的值"
myset1 = set([1,2,3,4,5,6])
myset2 = set([4,5,6,7,8,9])

print myset1 & myset2