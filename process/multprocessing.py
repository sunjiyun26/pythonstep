#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
from multiprocessing import Process
import  os
# print 'process (%s) start' % os.getpid()
# pid = os.fork()
# print pid
# if pid== 0:
#     print 'i am child prosss （%s） and my parent is %s' % os.getpid(),os.getppid()
# else:
#     print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)


def run_proc(name):
    print 'run child pross %s (%s)' % (name,os.getpid())

if __name__ =="__main__":
    print 'Parent process',os.getpid()
    p = Process(target=run_proc,args=('test',))
    print "process will start"
    p.start()
    p.join()
    print "process end"