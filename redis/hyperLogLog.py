# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2020/5/8 9:56
desc: HyperLogLog数据结构
"""
from mySentinel import *

# 主库实例
master = get_master()
slave = get_slave()
print(master,slave)
# hyperLogLog测试
key = 'codehole'
master.delete(key)

# 测试一
def test1(num):
	for i in range(num):
		master.pfadd(key, 'user%d'%i)
		total = slave.pfcount(key)
		if total != i+1:
			print(total,i+1)
			break

# 测试二
def test2(num):
	for i in range(num):
		master.pfadd(key, 'user%d'%i)
	print(num,slave.pfcount(key))

if __name__ == '__main__':
	# test1(1000)
	test2(100000)