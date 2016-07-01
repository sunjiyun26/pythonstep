#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
from collections import namedtuple

MynameTuple = namedtuple("point",["x","y"])
mynameTuple = MynameTuple(1,2)

print mynameTuple.x,mynameTuple.y

Circle = namedtuple("Circle",['x','y','r'])
circle =  Circle('1','2','3')
print  circle.r

print 'is instance of MynameTuple>>>>>>>>>>>>>>>>>>> ',isinstance(mynameTuple,MynameTuple)
print 'is instance of MynameTuple>>>>>>>>>>>>>>>>>   ',isinstance(mynameTuple,tuple)