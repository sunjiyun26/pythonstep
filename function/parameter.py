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
print '''һ�Ǳ�ѡ������ǰ��Ĭ�ϲ����ں󣬷���Python�Ľ������ᱨ��˼��һ��ΪʲôĬ�ϲ������ܷ��ڱ�ѡ����ǰ�棩��

�����������Ĭ�ϲ�����

�������ж������ʱ���ѱ仯��Ĳ�����ǰ�棬�仯С�Ĳ����ź��档�仯С�Ĳ����Ϳ�����ΪĬ�ϲ�����'''


def enroll(name,gender,age=6,address="jinan"):
	print 'name',name
	print 'gender',gender
	print 'age',age
	print 'address',address
	
enroll('sunjiyun','M')
enroll('sunjiyun','M',31)

print '''Ҳ���Բ���˳���ṩ����Ĭ�ϲ�����������˳���ṩ����Ĭ�ϲ���ʱ����Ҫ�Ѳ�����д�ϡ�'''

enroll('sunjiyun','M',address='jining')
	    

print '>>>>>>>>>'*10
print '��������Ĳ���Ĭ��ֵ��һ��������һ��ע�⣬������һ�� ָ������'

def addEndElement(mylist=[]):
    mylist.append("element")
    print mylist

addEndElement([1,2,31])
addEndElement(['sunjiyun','liutao','langchao'])
addEndElement()
addEndElement()
print '���������������˰�'
print '���岻��Ķ��� '
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
