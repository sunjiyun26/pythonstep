#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import itertools

natural = itertools.count(1)
for n in natural:
    # print n
    pass
nchar = itertools.cycle("abc")
for n in nchar:
    # print n
    pass
nrepeat = itertools.repeat("a",10)
for n in  nrepeat:
    print n