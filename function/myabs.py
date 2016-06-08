#!/usr/bin/env python
# -*- coding:utf-8 -*-
print '''当传入了不恰当的参数时，内置函数abs会检查出参数错误，
而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善'''

print '数据类型检查可以用内置函数isinstance()实现：'
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print '正常的参数',my_abs("2")
#my_abs("sunjiyun")