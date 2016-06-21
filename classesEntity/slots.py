#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
from types import MethodType

print 'slots 意思是 把…纳入其'


class Student(object):
    pass
    # __slots__ = ("name","age")
    # def __init__(self,name):
    #     self.name ="sunjiyun"
    #     print "test abc"


class StudentSlots(object):
    __slots__ = ("name", "age")


class SubStudentSlots(StudentSlots):
    pass


if __name__ == "__main__":
    def setAge(self, age):
        self.age = age
        print(self.age)


    student = Student()
    student.name = "sunjiyun pass"
    student.set_age = MethodType(setAge, student, Student)  # 给具体某个实例绑定一个方法
    student.set_age(31)
    print student.name
    print student.age

    print("绑定给一个实例的方法在另外一个实例上是不起作用的,AttributeError: 'Student' object has no attribute 'set_age'")
    student2 = Student()
    # student2.set_age(25)

    print("给class 绑定就所有都有了")
    Student.set_age = MethodType(setAge, None, Student)
    student2.set_age(25)

    print()
    print '__slots__ 来了'

    studentslots = StudentSlots()
    studentslots.name = "sunjiyun slots"
    studentslots.age = "31"
    print  "AttributeError: 'StudentSlots' object has no attribute 'score'"
    # studentslots.score = 98

    print '对子类不起作用'
    substudentslots = SubStudentSlots()
    substudentslots.name = "sunjiyun subslots"
    substudentslots.score = 98
    print  substudentslots.score
