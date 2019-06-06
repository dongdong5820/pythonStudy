# coding:utf-8

class Student(object):
	def __init__(self,name):
		self.name = name
	
	#print实例对象时调用
	def __str__(self):
		return 'Student object (name:%s)'%self.name
	
	#析构函数，类实例的引用全部被删除时调用
	def __del__(self):
		print('del success!')

	#实例被当做方法调用时调用该方法
	def __call__(self):
		return 'My name is %s'%self.name

	#调用不存在的属性时调用该方法
	def __getattr__(self, attr):
		print('属性%s不存在，这里返回默认值'%attr)
		if attr == 'score':
			return 100
		elif attr == 'age':
			return 18
		elif attr == 'hobby':
			return ['python','php','c++']		
		raise AttributeError('\'Student\' object has no attribute \'%s\''%attr)

#斐波拉契类
class Fib(object):
	def __init__(self):
		self.a, self.b = 0,1 #初始化两个计数器a,b
		
	#类被迭代时调用
	def __iter__(self):
		return self		#实例本身就是迭代对象，故返回自己

	#调用next()方法，或被迭代时返回下一个值
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b # 计算下一个值
		if self.a > 10000:
			raise StopIteration()
		return self.a # 返回下一个值
	
	#像list那样取第n个元素或切片时调用
	def __getitem__(self, n):
		if isinstance(n, int):	#n是索引
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a
		if isinstance(n, slice): #n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b = 1,1
			L = []
			for x in range(stop):
				if x >=start:
					L.append(a)
				a,b = b,a+b
			return L

#实现Chain().users('michael').repos输出/users/michael/repos
class Chain(object):
	def __init__(self,path=''):
		self.__path = path
	
	def __getattr__(self, path):
		return Chain('%s/%s'%(self.__path, path))

	def __call__(self, path):
		return Chain('%s/%s'%(self.__path, path))

	def __str__(self):
		return self.__path
	__repr__ = __str__


if __name__ == '__main__':
	s = Student('Jack')
	print(s)
	print(s())
	print(s.score)
	print(s.age)
	print(s.hobby)

	print('#循环定制类Fib:')
	for n in Fib():
		print(n, end=',')
	print()
	print('#像list一样操作Fib:')
	f = Fib()
	print('Fib[0]=%d'%f[0])
	print('Fib[10]=%d'%f[10])
	print('Fib[4:15]=%s'%f[4:15])
	print(Chain().users('michael').repos)
