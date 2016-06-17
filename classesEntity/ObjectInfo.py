#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import types

print u'首先，我们来判断对象类型，使用type()函数：'
print type("123")
print type(123)
print type(None)
print type(abs)

print type(123) == types.IntType
print type("123") == types.IntType
print type("123") == types.StringType, "\n"
print type(int) == type(str) == types.TypeType

print dir(str)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def __len__(self):
        return 99


if __name__ == '__main__':
    student = Student('sunjiyun', {'age': 31})
    print len(student)
    print u'判断是否含有attr hasattr'
    print hasattr(student, "name")
    print u'set attribute with setattr '
    print 'hasattr(student,"score")', hasattr(student, 'score')
    setattr(student, 'score','80')
    print 'after setattr hasattr(student,"score")', hasattr(student, 'score')
    print getattr(student,'score')
    print 'do you know what mean below'
    print getattr(student,'address','jinan')
