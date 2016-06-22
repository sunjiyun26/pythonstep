#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'

def helloWorld(self, name="world"):
    print 'hello ,%s' % name
if __name__ == "__main__":
    HelloWorld = type('HELLO2', (object,),dict(helloWorld2 = helloWorld))
    hello2 =  HelloWorld()
    # hello2.
class ListMetaclass(type):
    print "metaclass is from type"
    def __new__(cls, *args, **kwargs):
        pass


