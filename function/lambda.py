#!/usr/bin/env python
# -*- coding:utf-8 -*-
print '匿名函数的标志位lambda'
print map(lambda x: x*x ,[1,2,3,4,5])
print '匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量'
f=lambda x: x*x*x
print f(5)
