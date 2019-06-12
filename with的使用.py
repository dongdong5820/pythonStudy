#!/usr/bin/env python
#coding:utf-8

''' 
with的使用
with 表达式 as target：
	语句块
注释: 紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被>赋值给as后面的变量。当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法
'''

class Sample:
	def __enter__(self):
		print('In __enter__()')
		return 'Foo'

	def __exit__(self, type, value, trace):
		print('In __exit__()')

def get_sample():
	return Sample()

with get_sample() as f:
	print('sample:',f)

'''
with后面的代码块抛出任何异常时，__exit__()方法被调用
'''
class Sample2:
	def __enter__(self):
		return self

	def __exit__(self, type, value, trace):
		print('type:%s'%type)
		print('value:%s'%value)
		print('trace:%s'%trace)

	def doSomething(self):
		bar = 1/0
		return bar + 10
print('----with处理异常:')
with Sample2() as f:
	f.doSomething()

