#coding:utf-8

class Student(object):
	count = 0
	def __init__(self,name,score,age,sex):
		self.name = name
		self.score = score
		self.__age = age
		self.__sex = sex
		Student.count += 1
	
	def printScore(self):
		print('%s:%s'%(self.name, self.score))

	def setAge(self,age):
		if 0<age<=100:
			self.__age = age
		else:
			raise ValueError('bad age!')
	
	def getAge(self):
		return self.__age

s1 = Student('Jack', 90, 18, '男')
print('Student类实例个数：%d'%Student.count)
print(s1.name)
print(s1._Student__sex)
s1.setAge(19)
print(s1.getAge())
s2 = Student('Jim', 86, 20, '男')
print('Student类实例个数：%d'%Student.count)

class Father(object):
	def func(self):
		print('Father fun')

class Mother(object):
	def func(self):
		print('Mother fun')

class Son(Father,Mother):
	def test(self):
		super().func()
# __mro__ 查看类继承顺序
print(Son.__mro__)
s1 = Son()
print(s1.test())
