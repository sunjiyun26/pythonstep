#!/usr/bin/env python
# -*- coding:utf-8 -*-
def power(x):
    return x*x
print power(5)

print ""
print ">>>>>>>>>>"*5
print "next powern powern(x,n)"

def powern(x,n):
	num = 1
	while n>0:
		num = num*x
		n = n-1
	return num
    

powern(5,3)

print ""
print ">>>>>>>>>>"*5
print "next powern powern(x,n)  with default paramater n =2"
def powernDefault(x, n =2):
    num = 1
    while n>0:
	    num = num*x
	    n =  n-1
    return num
   
print 'powernDefault(2,4)',powernDefault(2,4)
print 'powernDefault(2)',powernDefault(2)

print '>>>>>>>>>'*10
print '''一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。'''


def enroll(name,gender,age=6,address="jinan"):
	print 'name',name
	print 'gender',gender
	print 'age',age
	print 'address',address
	
enroll('sunjiyun','M')
enroll('sunjiyun','M',31)

print '''也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。'''

enroll('sunjiyun','M',address='jining')
	    

print '>>>>>>>>>'*10
print '如果函数的参数默认值是一个变量，一定注意，变量是一个 指针索引'

def addEndElement(mylist=[]):
    mylist.append("element")
    print mylist

addEndElement([1,2,31])
addEndElement(['sunjiyun','liutao','langchao'])
addEndElement()
addEndElement()
print '哈哈哈，出问题了吧'
print '定义不变的东西 '
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    print L
    return
add_end([1,2,31])
add_end(['sunjiyun','liutao','langchao'])
add_end()
add_end()
