#!/usr/bin/env python
# -*- coding:utf-8 -*-
print '�ؼ��ֲ��� '
def person(name,age,**keysword):
    print 'name:',name,'age:',age,'other:',keysword

person('sunjiyun','31')
person('sunjiyun','31',address='jinan',gender='man')

print '�Ϳɱ�������ƣ�Ҳ��������װ��һ��dict��Ȼ�󣬰Ѹ�dictת��Ϊ�ؼ��ֲ�������ȥ��'
dictNew = {"address":'jinan',"gender":'male'}
person('sunjiyun','31',**dictNew)
print '��kw��õ�dict��extra��һ�ݿ�������kw�ĸĶ�����Ӱ�쵽�������extra��'

print '�����ؼ��ֲ���'
