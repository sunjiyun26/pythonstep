#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import codecs
try:
    f = open("ReportDisplay.java",'r')
    # print 'read 20 bytes',f.read(20)
    print '读取一行',f.readline()
    for line in f.readline():
        print line.strip()
    print '读取2行',f.readline()

    print()
    print ("二进制 例如读取图片")
    fjpg = open(u"QQ图片20160608104955.jpg",'rb')
    print fjpg.read()

    print "write file"
    fw =open("ceshi.txt","w")
    fw.write("cesshi")
    fw.close()

    with codecs.open('ceshi.txt', 'r', 'gbk') as f2:
        print f2.read() # u'\u6d4b\u8bd5'
        f2.close()
    with open('test.txt', 'w') as fw2:
        fw2.write('Hello, world!')
        fw2.close()

finally:
    f.close()
    fjpg.close()