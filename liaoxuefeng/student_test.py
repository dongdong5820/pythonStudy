#!/usr/bin/env python
#coding:utf-8

import unittest
from student import Student
'''
针对student学生类写的单元测试用例
单元测试执行命令: python3 -m unittest student_test
'''
class TestStudent(unittest.TestCase):
	def test_80_100(self):
		s1 = Student('Jim', 80)
		s2 = Student('Terry', 100)
		self.assertEqual(s1.get_grade(), 'A')
		self.assertEqual(s2.get_grade(), 'A')
	
	def test_60_80(self):
		s1 = Student('Tom', 60)
		s2 = Student('Jack', 79)
		self.assertEqual(s1.get_grade(), 'B')
		self.assertEqual(s2.get_grade(), 'B')
	
	def test_0_60(self):
		s1 = Student('Tom', 10)
		s2 = Student('Jack', 57)
		self.assertEqual(s1.get_grade(), 'C')
		self.assertEqual(s2.get_grade(), 'C')

	#测试不合法的成绩
	def test_invalid(self):
		s1 = Student('Tom', -1)
		s2 = Student('Jack', 101)
		with self.assertRaises(ValueError):
			s1.get_grade()
		with self.assertRaises(ValueError):
			s2.get_grade()
		
if __name__ == '__main__':
	unittest.main()
