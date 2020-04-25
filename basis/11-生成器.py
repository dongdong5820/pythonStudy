#coding:utf-8
from generators import *

#调用表达式生成的generator
g = gen_expr(10)
print(g)
for x in g:
	print(x)

print('--'*30)
#调用函数生成的generator
g1 = gen_fun(10)
print(g1)
x=0
while x < 10:
	print(g1.__next__())
	if x == 5:
		print(g1.send(100))
	x+=1


