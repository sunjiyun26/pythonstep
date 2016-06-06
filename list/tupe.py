#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
print 'tupe 和list 的区别是 tupe一旦定义 其内容是不可变的 '

print 'def tupe like this tupe(1,2,3,\'sunjiyun\')'
_tupe = (1,2,3,"sunjiyun")
print _tupe
print '_tupe 的第一个元素是 tupe[0]:',_tupe[0]
print '_tupe 的倒数第一个元素是 tupe[-1]:',_tupe[-1]
tupeBlank = ()
print '一个空的tupe 是 tupeBlank = ():',tupeBlank
tupeOneElement = (1,)
print '一个空的tupe 是 tupeOneElement = (1,):',tupeOneElement

print '还有没写完的 到底 tupe内部有list 的时候能不能修改呢？'