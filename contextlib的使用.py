#!/usr/bin/env python
#coding:utf-8

from contextlib import closing
'''
contextlib.closing()会帮后面对象加上__enter__()和__exit__()方法，使其满足with的条件
'''

class Door(object):
	def open(self):
		print('Door is opened')

	def close(self):
		print('Door is closed')

with closing(Door()) as f:
	f.open()
