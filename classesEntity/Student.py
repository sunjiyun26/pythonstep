#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'


class Student(object):
    def __init__(self):
        self.name = "sunjiyun"
        self.age = 31
        self.score = 90

    def printSelf(self):
        print self.name, self.age, self.score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


class Student2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printSelf(self):
        print  self.age, self.name


class Student3(Student):
    def printSelf(self):
        self.age = 80
        print  '%s,%s,123' % (self.name, self.age)
        # pass
        # def __init__(self,name,age,score):
        #   pass


if __name__ == "__main__":
    student = Student()
    student.printSelf()
    print student.get_grade()

    student2 = Student2('sunjiyun', '6')
    student2.printSelf()

    student3 = Student3()
    student3.printSelf()
    print(student3.get_grade())

    print 'student isinstance Student',isinstance(student,Student),"\n"
    print 'student2 isinstance Student',isinstance(student2,Student),"\n"
    print 'student3 isinstance Student',isinstance(student3,Student),"\n"
    print 'student isinstance Student3 ',isinstance(student,Student3),"\n"

    print 'student3 isSubClass Student',issubclass(Student3,Student),"\n"
    print 'student2 isSubClass Student',issubclass(Student2,Student),"\n"


