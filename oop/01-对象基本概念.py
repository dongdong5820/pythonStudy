class Person(object):
	# 创建对象时调用
	def __new__(cls, name, sex):
		print('调用自己的构造方法创建对象')
		return object.__new__(cls)

	# 初始化方法
	def __init__(self, name, sex):
		self.name = name
		self.sex = sex

	# 打印类的对象时调用，该方法必须返回一个字符串
	def __str__(self):
		return '我是%s,我的性别%s' % (self.name, self.sex)

	# 析构函数，当类的对象的所有引用被删除时调用
	def __del__(self):
		print('%s对象引用全被删除，执行析构函数' % self.name)


# __new__,__init__,__str__,__del__已两个下划线开始，两个下划线结束的方法都叫魔术方法，不会调用，程序会在特定情况下自动调用


p1 = Person('laoxiao', '男')
p2 = Person('xiaoli', '女')
p3 = p1
print(id(p1))
print(id(p2))
print(id(p3))
del (p1)
print(p2)
del (p3)
