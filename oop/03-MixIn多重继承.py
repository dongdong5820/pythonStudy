#coding:utf-8

'''
类的多重继承:一个类继承多个类。python本身支持多重继承。php本身不支持，但是trait可以实现php的多重继承
'''

#动物类
class Animal(object):
	pass

#哺乳类
class Mammal(Animal):
	pass

#鸟类
class Bird(Animal):
	pass

#能跑类
class RunnableMixIn(object):
	def run(self):
		print('Running...')

#能飞类
class FlyableMixIn(object):
	def fly(self):
		print('Flying...')

#狗(多重继承)
class Dog(Mammal,RunnableMixIn):
	pass

#蝙蝠(多重继承)
class Bat(Mammal,FlyableMixIn):
	pass

#鹦鹉(多重继承)
class Parrot(Bird, FlyableMixIn):
	pass

#鸵鸟(多重继承)
class Ostrich(Bird, RunnableMixIn):
	pass

print(Dog.__mro__)
print(Ostrich.__mro__)
