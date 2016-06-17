#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
print '访问限制'


class Student(object):
    def __init__(self):
        self.__name = 'sunjiyun'
        self.__age = 30

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age

    def setName(self):
        self.__name = 'john'

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


if __name__ == "__main__":
    student = Student()
    print student.getname(), ">>>>>>>>>>>>>", student.getage()
    student.setName()
    # student.set_score(102)
    print "after changed",student.getname()
    print ''
    print 'student.__name error AttributeError: \'Student\' object has no attribute \'__name\''
    # print student.__name
    print 'you can access it like this student._Student__name'
    print student._Student__name

    print isinstance(student,Student)
