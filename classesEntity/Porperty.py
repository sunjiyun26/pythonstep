#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'


class Student:
    def get_Score(self):
        return self.score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be in t type")
        if score < 0 or score > 100:
            raise ValueError("score must between 0 and 100")
        self.score = score


class StudentProperty:
    @property
    def score(self):
        return self.score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError(" score must be a int type")
        if score < 0 or score > 100:
            raise ValueError("score must between 0 and 100")
        self.score = score


class StudentBirth(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2016 - self.birth


if __name__ == "__main__":
    student = Student()
    student.set_score(23)
    print student.get_Score()

    # student.set_score("123")
    # student.set_score(101)
    # student.set_score(-1)

    studentProperty = StudentProperty()
    studentProperty.score = 90
    print studentProperty.score

    studentBirth = StudentBirth()
    studentBirth.birth = 1985
    print studentBirth.age
