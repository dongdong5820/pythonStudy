#coding:utf-8

class Student(object):
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value

	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self, birth):
		self._birth = birth

	@property
	def age(self):
		return 2019 - self._birth 

s = Student()
s.score = 80
print('score:%s'%s.score)
s.birth = 1989
print(s.birth) 
print(s.age) 
