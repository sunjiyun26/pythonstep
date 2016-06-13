#!/usr/bin/python
__author__ = 'sunjiyun'
def functionMutile(a,b,c=0,*args,**kwargs):
    print 'a=',a,'b=',b,'c=',c,'args=',args,'kwargs=',kwargs

functionMutile(1,2)
functionMutile(1,2,3,[4,5,6])
functionMutile(1,2,3,[4,5,6],name='sunjiyun')
