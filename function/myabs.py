#!/usr/bin/env python
# -*- coding:utf-8 -*-
print '''�������˲�ǡ���Ĳ���ʱ�����ú���abs�������������
�����Ƕ����my_absû�в�����飬�ᵼ��if������������Ϣ��abs��һ�������ԣ�����������岻������'''

print '�������ͼ����������ú���isinstance()ʵ�֣�'
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print '�����Ĳ���',my_abs("2")
#my_abs("sunjiyun")