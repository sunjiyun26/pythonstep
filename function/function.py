#!/usr/bin/env python
# -*- coding:utf-8 -*-
print 'python 的函数调用 错误提示非常的有好'
print 'abs() ',abs(-123)
print 'cmp(1,2) ',cmp(1,2)
print 'cmp(2,1) ',cmp(2,1)
print 'cmp(2,2) ',cmp(2,2)

print 'datatype convert is int(),str(),float(),unicode,str'

print '可以把一个变量指向一个函数 然后用这个变量就行调用函数 例如 a = abs, a(-1),是不是像js 的语法呢'
a = abs
print a(-7)

print '>>'*10
print ("定义函数")
def myfunction():
    print 'myfunction'
myfunction()


print '>>'*10
print ("定义函数 含有 return, 如果不写 return none")
def myFunctionReturn():
    return 10
print "the return function returns number 10 ",myFunctionReturn()

print '如果打印的是函数名 例如 print myFunctionReturn 而不是 myFunctionReturn() 则打印如下  <function myFunctionReturn at 0x029AC3F0> ',myFunctionReturn

print '>>'*10
print ("定义空函数 with pass ")
def blankFunction():
    pass
print ('pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。')
print '''if age >= 18:
    pass'''