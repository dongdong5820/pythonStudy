# coding:utf-8

import functools

#完整装饰器
def log(text):
	if isinstance(text,str):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print('%s begin call %s():'%(text,func.__name__))
				fe = func(*args,**kw)
				print('%s end call %s():'%(text,func.__name__))
				return fe
			return wrapper
		return decorator
	else:
		@functools.wraps(text)
		def wrapper(*args,**kw):
			print('begin call %s():'%text.__name__)
			fe = text(*args,**kw)
			print('end call %s():'%text.__name__)
			return fe
		return wrapper

@log
def f1():
	print('I am %s.'%f1)

@log('excute')
def f2():
	print('I am %s.'%f2)

if __name__ == '__main__':
	f1()
	f2()
