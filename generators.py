# coding:utf-8
#generator expression(生成器表达式)
def gen_expr(num):
	a = (x for x in range(0,num))
	return a

#用函数生成generator
def gen_fun(num):
	x = 0
	while x < num:
		yield x**2	#yield(放弃)，函数在此地方交出CPU控制权(停止运行)。 在调用next(),send()方法时再往下执行
		x+=1
	return 

if __name__ == '__main__':
	g1 = gen_fun(5)
	print(g1)
