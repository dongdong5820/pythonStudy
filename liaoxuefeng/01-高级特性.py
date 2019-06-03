#!/usr/bin/env python3
#coding:utf-8

#利用切片操作，实现一个trim()函数，去除字符串首尾空格，注意不要调用str的strip()方法
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

#函数迭代器
def g():
	yield 1
	yield 2
	yield 3

#使用迭代查找一个list中最小值和最大值，并返回一个tuple
def findMinAndMax(L):
	if len(L) == 0:
		min=None
		max=None
	else:
		min=max=L[0]
		for x in L:
			if x < min:
				min = x
			if x > max:
				max = x
	
	return (min,max)

#使用生成器，生成杨辉三角数列
def triangles():
	p = [1]
	while True:
		yield p
		p = [1] + [p[n]+p[n+1] for n in range(len(p)-1)] + [1]
 
if __name__ == '__main__':
	print('--'*20+'切片')
	L = ['Michael','Sarah','Tracy','Bob','Jack']
	print('L=', L)
	print('L[0:3]=',L[0:3])
	print('L[:3]=', L[:3])
	print('L[1:3]=',L[1:3])
	print('L[-2:]=', L[-2:])

	if trim('hello ') != 'hello':
	    print('1测试失败！')
	if trim(' hello') != 'hello':
	    print('2测试失败！')
	if trim(' hello ') != 'hello':
	    print('3测试失败！')
	if trim(' hello world ') != 'hello world':
	    print('4测试失败！')
	if trim('') != '':
	    print('5测试失败！')
	if trim('   ') != '':
	    print('6测试失败！')
	print('测试成功！')

	print('--'*20+'迭代')
	from collections import Iterable,Iterator
	print('Iterable:可迭代对象')
	print('Iterable? [1,2,3]:',isinstance([1,2,3], Iterable))
	print('Iterable? \'abc\':', isinstance('abc', Iterable))
	print('Iterable? 123:', isinstance(123, Iterable))
	print('Iterable? g():', isinstance(g(), Iterable))
	print('Iterator:迭代器')
	print('Iterator? [1,2,3]:',isinstance([1,2,3], Iterator))
	print('Iterator? iter([1,2,3]):',isinstance(iter([1,2,3]), Iterator))
	print('Iterator? \'abc\':', isinstance('abc', Iterator))
	print('Iterator? 123:', isinstance(123, Iterator))
	print('Iterator? g():', isinstance(g(), Iterator))
	l = [1,2,3,4,5]
	print('#iter list:%s'%l)
	print('for x in :%s'%l)
	for x in l:
		print(x)
	print('for x in iter(%s):'%l)
	for x in iter(l):
		print(x)
	print('nex():')
	it = iter(l)
	print(next(it))	
	print(next(it))	
	print(next(it))	
	print(next(it))	
	print(next(it))	
	d = {'a':1, 'b':2, 'c':3}
	print('#iter each key:', d)
	for k in d.keys():
		print('key:', k)
	print('#iter each value:', d)
	for v in d.values():
		print('value:', v)
	print('#iter both key and value:', d)
	for k,v in d.items():
		print('item:', k,v)
	print('#iter list with index:')
	l = ['A','B','C']
	print('iter enumerate(%s):'%l)
	for i ,value in enumerate(l):
		print(i,value)
	print('#iter complex list:')
	cl = [(1,1),(2,4),(3,9)]
	print('iter %s:'%cl)
	for x,y in cl:
		print(x,y)
	print('#查找列表最小和最大值并返回')
	print('findMinAndMax[]:',findMinAndMax([]))
	print('findMinAndMax[7]:',findMinAndMax([7]))
	print('findMinAndMax[1,93,4,5]:',findMinAndMax([1,93,4,5]))

	print('--'*20, '列表生成式')
	import os
	print('#运用列表生成式，列出当前目录下的所有文件和目录名:')
	[d for d in os.listdir('.')]
	L1 = ['Hello','World',18,'Apple',None]
	L2 = [s.lower() for s in L1 if isinstance(s,str)]
	print(L2)

	print('--'*20, '生成器')
	n = 0 
	results = []
	for t in triangles():
		print(t)
		results.append(t)
		n+=1
		if n == 10:
			break;
