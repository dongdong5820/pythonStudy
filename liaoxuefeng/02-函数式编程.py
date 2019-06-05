#!/usr/bin/env python3
#coding:utf-8

from functools import reduce

#利用map函数，把用户输入的不规范英文名字，变成首字母大写，其他小写的规范名字
def normalize(name):
	name = name[0].upper() + name[1:].lower()
	return name

#sum()函数接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce求积
def prod(l):
	return reduce(lambda x,y:x*y, l)

#以3开头的奇数序列
def _odd_iter():
	n = 1
	while True:
		n = n+2
		yield n
#定义一个筛选函数
def _not_divisible(n):
	return lambda x : x % n > 0

#利用filter()函数求素数
def primes():
	yield 2
	it = _odd_iter() #初始序列
	while True:
		n = next(it) #返回序列的第一个数
		yield n
		it = filter(_not_divisible(n), it) #构造新序列

#求max以内的所有回数（左右对称的数，如12321,909）
def palindrome(max):
	def is_symmetry(n):
		return n == int(str(n)[::-1])
	return list(filter(is_symmetry, range(1,max)))

#利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
	L[0] = 0	
	def counter():
		L[0] = L[0] + 1
		return L[0]
	return counter

if __name__ == '__main__':
	print('--'*20+'高阶函数')
	print('#map()函数的应用：')
	L1 = ['adam','LISA','barT']
	L2 = list(map(normalize,L1))
	print(L1,L2)
	print('#reduce函数的应用：')
	L1 = [1,2,3,4,5]
	L2 = prod(L1)
	print(L1,L2)
	L = []
	max = 100
	print('#filter()函数的应用：')
	for n in primes():
		if n < max:
			L.append(n)
		else:
			break
	print('%d以内的素数列表:%s'%(max,L))
	print('%d以内的回数列表:%s'%(max,palindrome(max)))
	print('#sorted()函数的应用：')
	L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
	print('%s按照成绩降序结果：%s'%(L, sorted(L, key=lambda s:s[1],reverse=True)))
	print('#闭包的应用：')
	c1 = createCounter()
	print(c1())	
	print(c1())	
	print(c1())	
