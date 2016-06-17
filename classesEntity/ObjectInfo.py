#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import types

print u'首先，我们来判断对象类型，使用type()函数：'
print type("123")
print type(123)
print type(None)
print type(abs)

print type(123) == types.IntType
print type("123") == types.IntType
print type("123") == types.StringType,"\n"
print type(int) == type(str) == types.TypeType

print dir(str)

