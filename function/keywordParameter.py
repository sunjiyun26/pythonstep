#!/usr/bin/env python
# -*- coding:utf-8 -*-
print '关键字参数 '
def person(name,age,**keysword):
    print 'name:',name,'age:',age,'other:',keysword

person('sunjiyun','31')
person('sunjiyun','31',address='jinan',gender='man')

print '和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：'
dictNew = {"address":'jinan',"gender":'male'}
person('sunjiyun','31',**dictNew)
print '意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。'

print '命名关键字参数'
