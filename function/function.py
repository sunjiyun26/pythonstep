#!/usr/bin/env python
# -*- coding:utf-8 -*-
print 'python �ĺ������� ������ʾ�ǳ����к�'
print 'abs() ',abs(-123)
print 'cmp(1,2) ',cmp(1,2)
print 'cmp(2,1) ',cmp(2,1)
print 'cmp(2,2) ',cmp(2,2)

print 'datatype convert is int(),str(),float(),unicode,str'

print '���԰�һ������ָ��һ������ Ȼ��������������е��ú��� ���� a = abs, a(-1),�ǲ�����js ���﷨��'
a = abs
print a(-7)

print '>>'*10
print ("���庯��")
def myfunction():
    print 'myfunction'
myfunction()


print '>>'*10
print ("���庯�� ���� return, �����д return none")
def myFunctionReturn():
    return 10
print "the return function returns number 10 ",myFunctionReturn()

print '�����ӡ���Ǻ����� ���� print myFunctionReturn ������ myFunctionReturn() ���ӡ����  <function myFunctionReturn at 0x029AC3F0> ',myFunctionReturn

print '>>'*10
print ("����պ��� with pass ")
def blankFunction():
    pass
print ('pass���ʲô������������ʲô�ã�ʵ����pass����������Ϊռλ�����������ڻ�û�����ôд�����Ĵ��룬�Ϳ����ȷ�һ��pass���ô���������������')
print '''if age >= 18:
    pass'''