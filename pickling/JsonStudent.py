#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import  json
class Student:
    def __init__(self,name,age,score):
        self.name =name
        self.age = age
        self.score =score
def student2dict(std):
     return {
         'name':std.name,
         'age':std.age,
         'score':std.score
        }
def loadStudent(std):
    return Student(std['name'],std['age'],std['score'])

student = Student("sunjiyun",31,'59')
print(json.dumps(student,default=student2dict))

print (json.dumps(student,default=lambda obj: obj.__dict__))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print (json.loads(json_str,object_hook=loadStudent))
