# 匿名函数应用
def fnc(x, y): return x + y


def test(x, y, func):
    return func(x, y)


#fn = input('请输入要合法的表达式：')
#fn = eval(fn)
print('表达式最后运算的结果是%s' % (test(20, 4, fnc)))
