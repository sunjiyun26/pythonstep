#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
from multiprocessing import Pool,Queue,Process
import os, random, time

print("%s 进程间通信是通过Queue、Pipes等实现的" % os.getpid())

def longChildProcess(name):
    print 'run task %s %s....' % (name, os.getpid())
    starttime = time.time()
    time.sleep(random.random() * 3)
    endtime = time.time()
    print 'it takes about: ', endtime - starttime, ' s '

def writeQueue(q):
    for val in ['A','B','C']:
        print 'put value %s to queue' % val
        q.put(val)
        time.sleep(random.random())

def readQueue(q):
    while True:
        value=  q.get(True)
        print("get value %s" % value)
if __name__ == "__main__":
    print 'parent process id is %s' % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(longChildProcess, args=(i,))
    print " %s parent waiting for all child process" % os.getpid()
    p.close()
    p.join()
    print "parnet end "

# 创建队列
    q= Queue()
    # 创建两个进程
    processWrite = Process(target=writeQueue,args=(q,))
    processRead = Process(target=readQueue,args=(q,))
    # 启动进程
    processWrite.start()
    processRead.start()

    processWrite.join()
    processRead.terminate()

