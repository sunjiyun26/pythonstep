#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import time,random,threading

def threadRun():
    print "我是子线程 %s.... " % threading.current_thread().getName()
    n = 0
    while n<5:
        n =n+1
        print "thread %s >>>>%s" % (threading.currentThread().getName(),n)
        time.sleep(10)
    print "now this threand name %s" % threading.currentThread().getName()


if __name__ =="__main__":
    print "threading is running %s" % threading.currentThread().getName()
    t = threading.Thread(target=threadRun,name="sunjiyunThread")


    t2 = threading.Thread(target=threadRun,name="sunjiyunThread2")
    t.start()

    t2.start()
    t.join()
    t2.join()
    print 'thread is end %s' % threading.currentThread().getName()


