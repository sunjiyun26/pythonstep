#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

def firstModule():
    args = sys.argv
    print 'diyigemokuai'
    print ('canshu changdu ',len(args))
    if len(args) == 1:
        print("only one param")
    elif len(args) == 2:
        print('hello',args[1])
    else:
        print(args)
def cStringIO():
    steio = StringIO.StringIO("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print steio

if __name__ =='__main__':
    firstModule()
    cStringIO()