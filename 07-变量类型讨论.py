#x为不可变类型，调用函数的时候a引用指向值为2的内存，函数执行成功后a执行值为4的内存。x的引用没变还是指向值为2的内存
def test(a):
	a+=a
	print(a)

x=2
test(x)
print(x)
print("="*30)

