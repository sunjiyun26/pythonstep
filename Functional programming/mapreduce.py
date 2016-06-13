#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'


def _myfunction(x):
    return x * x

def add(x,y):
    return x+y

print u'调用自己的方法 _myfunction', map(_myfunction, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print u'调用 str', map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print u'调用 int', map(int, ["1", "2", "3", "4"])

print u'调用reduce', reduce(add, [1, 2, 3, 4])
print reduce(add, [1, 2, 3, 4])

def fn(x,y):
    return x*10+y
def str2int():
    return {"0":1,"1":1,"2":2,"3":3,"3":3,"4":4,"5":1,"1":1,"1":1}

print reduce(fn,[1,3,5,7,9])

def convertUpLower(x):
    return x[0].upper()+x[1:len(x)].lower()
print map(convertUpLower,['adam', 'LISA', 'barT'])

def prod(x,y):
    return x*y
print(reduce(prod,[1,3,5,7]))
