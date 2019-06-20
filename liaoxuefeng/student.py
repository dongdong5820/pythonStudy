#!/usr/bin/env python
#coding:utf-8

'''
单元测试练习-学生类
'''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score > 100:
            raise ValueError('%d is invalid'%self.score)
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        if self.score < 0:
            raise ValueError('%d is invalid'%self.score)
        return 'C'

