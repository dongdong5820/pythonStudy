#!/usr/bin/env python
#coding:utf-8

'''
编写的这对mydict.Dict类的单元测试
执行单元测试命令(不要文件后缀名): python3 -m unittest mydict_test
'''

import unittest
from mydict import Dict

class TestDict(unittest.TestCase):
	#每个单元测试开始前执行代码块
	def setUp(self):
		print('setUp...')

	def test_init(self):
		d = Dict(a=1,b='test')
		#断言
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertTrue(isinstance(d,dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d['key'], 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d.key, 'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

	#每个单元测试结束后执行代码块
	def tearDown(self):
		print('tearDown')

if __name__ == '__main__':
	#运行单元测试
	unittest.main()	
