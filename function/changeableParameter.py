#!/usr/bin/env python
# -*- coding:utf-8 -*-
print '可变参数 '
def calChanged(numbers):
    sum = 0
    for num in numbers:
		sum = sum + num*num
    print sum
    return sum

calChanged([1,2,3,4])
calChanged((1,2,3,4))

print "可变参数 指的 可以在参数的前面加上一个 *，调用的时候就不用再写numbers"
def calChanged(*numbers):
    sum = 0
    for num in numbers:
		sum = sum + num*num
    print sum
    return sum
print '调用如下：calChanged(1,2,3)'
calChanged(1,2,3)
print '也可以不传参数，调用如下：calChanged()'
calChanged()

print '所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去'
numbersNew = (1,2,3,4)
calChanged(*numbersNew)
