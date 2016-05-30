#!/usr/bin/env python
# -*- coding:utf-8 -*- 
print '\'\' contains string'
print "\"\" contains string"
print '换行需要用斜杠n 进行转义 this is\n '
print '\需要转义“\\” 两个\ 表示 \\'
print '如果字符串里面有很多字符都需要转义，就需要加很多''\，为了简化，Python还允许用r''表示''内部的字符串默认不转义'
print r'\\\\this is not zhuanyi \\\\\\\   jjjjjj'
print "如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容 "
print '''abc
... def
... ghi'''
