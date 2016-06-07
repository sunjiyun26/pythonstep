#!/usr/bin/env python
# -*- coding:utf-8 -*-
print 'this is if ,在条件判断语句后面 需要加一个":" 就像{}一样'
age = 19  
if age < 18:
    print 'age is < 18'
    age = 20
    if age > 18:
	print 'chaged to > 18'
elif age > 20:
	print 'age  > 20'
else:
    print 'age is > 18 and age is <= 20'
	
print ">"*20

print " "*20

print '语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else'
print '''age = 20
 if age >= 6:
   print \'teenager\'
 elif age >= 18:
    print \'adult\'
 else:
    print \'kid\' '''

print " "*20
age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'

print '原来从raw_input()读取的内容永远以字符串的形式返回'
birth = raw_input()
print birth
birth = int(birth)
if birth>=1985:
    print '85 hou'
else:
	print '70hou'
	
