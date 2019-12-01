# coding:utf-8
'''
1、闭包：函数里面嵌套函数。并且内层函数要用到外层函数的参数。闭包延长外层函数变量的生命周期
2、装饰器：也是一种闭包。但是外层函数的参数也是一个函数
3、语法糖 @装饰器名称 如： @use_logging
'''

print('-'*20,'简单装饰器')
def use_logging(func):
	def wrapper():
		print('logging:%s is running'%func.__name__)
		return func()
	return wrapper

@use_logging
def foo():
	print('I am foo')

#f1 = use_logging(foo)
#f1()
foo()

print('-'*20,'带参数的业务函数')
def use_logging1(func):
	def wrapper(name):
		print('logging1:%s is running'%func.__name__)
		return func(name)
	return wrapper

@use_logging1
def foo1(name):
	print('I am %s'%name)

foo1('ranlay')

print('-'*20,'带多参的业务函数')
def use_logging2(func):
	def wrapper(*args, **kwargs):
		print('logging2:%s is running'%func.__name__)
		return func(*args, **kwargs)
	return wrapper

@use_logging2
def foo2(*args, **kwargs):
	print(args)
	print(kwargs)

foo2('ranlay',1200,3000,age=30,height=172)

print('-'*20,'带参数的装饰器')
def use_logging3(level):
	def decorator(func):
		def wrapper(*args, **kwargs):
			if level == 'warn':
				print('warn logging3:%s is running'%func.__name__)
			elif level == 'info':
				print('info logging3:%s is running'%func.__name__)
			else:
				print('error logging3:%s is running'%func.__name__)
			return func(*args, **kwargs)
		return wrapper
	return decorator

@use_logging3(level='warn')
def foo3(*args, **kwargs):
	print(args)
	print(kwargs)

foo3('laosu',120,300,age=20,height=172,weight=60)
