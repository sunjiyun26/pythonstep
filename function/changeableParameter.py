#!/usr/bin/env python
# -*- coding:utf-8 -*-
print '�ɱ���� '
def calChanged(numbers):
    sum = 0
    for num in numbers:
		sum = sum + num*num
    print sum
    return sum

calChanged([1,2,3,4])
calChanged((1,2,3,4))

print "�ɱ���� ָ�� �����ڲ�����ǰ�����һ�� *�����õ�ʱ��Ͳ�����дnumbers"
def calChanged(*numbers):
    sum = 0
    for num in numbers:
		sum = sum + num*num
    print sum
    return sum
print '�������£�calChanged(1,2,3)'
calChanged(1,2,3)
print 'Ҳ���Բ����������������£�calChanged()'
calChanged()

print '����Python��������list��tupleǰ���һ��*�ţ���list��tuple��Ԫ�ر�ɿɱ��������ȥ'
numbersNew = (1,2,3,4)
calChanged(*numbersNew)
