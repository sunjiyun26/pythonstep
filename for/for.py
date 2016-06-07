#!/usr/bin/env python
# -*- coding:utf-8 -*-
names = ['sunjiyun','liutao','hehaiwei']
for name in names:
    print name
sum =0 
for i in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum+i
print sum

print  range(5)
sum = 0
for x in range(101):
    sum+=x
print sum;

n = 100
sum = 0
while n>0:
    sum += n
    n = n-1
print n,sum