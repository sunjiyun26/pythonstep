#!/usr/bin/env python
# -*- coding:utf-8 -*-
mydict = {"name":"sunjiyun","age":'31',"tel":'13853197274','address':'shandong jinan'}
print mydict
print 'name is: ',mydict['name']
print 'add new element mydict[\'company\'] =  \'shandong\' '
mydict['company'] = 'company'
print mydict

print ">"*10
print "判断是否存在 用in  job in mydict"
print 'job' in mydict

print '如果不存在的话 KeyError: \'Thomas\''
#print mydict['job']

print ">"*10
print "get key"
print mydict.get("name")

print ">"*10
print "pop key"
print mydict.pop("name")
print "after pop name ",mydict