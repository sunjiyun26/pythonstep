#!/usr/bin/env python
# -*- coding:utf-8 -*-
print 'this is if ,�������ж������� ��Ҫ��һ��":" ����{}һ��'
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

print '���ִ���и��ص㣬���Ǵ��������жϣ������ĳ���ж�����True���Ѹ��ж϶�Ӧ�����ִ�к󣬾ͺ��Ե�ʣ�µ�elif��else'
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

print 'ԭ����raw_input()��ȡ��������Զ���ַ�������ʽ����'
birth = raw_input()
print birth
birth = int(birth)
if birth>=1985:
    print '85 hou'
else:
	print '70hou'
	
