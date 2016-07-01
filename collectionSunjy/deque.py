#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
from collections import deque

mydque = deque(['1','b','sunjiyun'])
print mydque
mydque.append("sunjiyun2")
print mydque
mydque.appendleft("left sunjiyun")
print mydque

