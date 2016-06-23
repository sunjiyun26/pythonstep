#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'


def div0():
    try:
        print 'try'
        value = 10 / 0
        print "10/0", value
    except ZeroDivisionError, e:
        print 'exception', e
    finally:
        print 'final'


def div1(i):
    print '有参数>>>>>>>>>>> ',i
    try:
        r = 10 / int(i)
        print 'result', r
    except ValueError, ex:
        print 'value error', ex
    except ZeroDivisionError, ex2:
        print 'zero valuueerror', ex2
    finally:
        print "final div01"


if __name__ == "__main__":
    div0()
    div1("abc")
    div1(2)
    div1(0)
