#coding:utf-8
from generators import *

#调用表达式生成的generator
g = gen_expr(10)
print(g)
for x in g:
	print(x)
