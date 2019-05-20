# coding:utf-8
#generator expression(生成器表达式)
def gen_expr(num):
	a = (x for x in range(0,num))
	return a

#用函数生成generator
def gen_fun(num):
	x = 0
	while x < num:
		a = yield x**2	#yield(放弃)，函数在此地方交出CPU控制权(停止运行)。 在调用next(),send()方法时再往下执行
		if a == 100:	#上行的a可以接受send(100)函数的传参.如100
			print('I am 100')
		else:
			x+=1

#裴波拉切generator
def gen_fib(num):
	x = 0
	a,b = 1,1
	while x < num:
		yield b
		a,b = b,a+b 
		x+=1

#直接执行此文件时如下代码会执行。若以模块形式导入该文件时如下代码不执行。 主要用于测试
if __name__ == '__main__':
	g1 = gen_fun(5)
	print(g1)
	print(g1.__next__())
	g1.send(100)
	print(g1.__next__())
	print('-'*50)
	g2 = gen_fib(5)
	print(g2)
	for i in g2:
		print(i)
