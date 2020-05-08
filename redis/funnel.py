# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2020/5/8 17:00
desc: 漏斗限流
"""
import time

class Funnel(object):
	def __init__(self,capacity,leaking_rate):
		# 漏斗容量
		self.capacity = capacity
		# 漏嘴流水速率
		self.leaking_rate = leaking_rate
		# 漏斗剩余空间
		self.left_quota = capacity
		# 上一次漏水时间
		self.leaking_ts = time.time()

	# 腾出空间（漏水）
	def make_space(self):
		now_ts = time.time()
		# 距离上一次漏水过去了多久
		delta_ts = now_ts - self.leaking_ts
		# 腾出的空间
		delta_quota = delta_ts * self.leaking_rate
		# 若腾出空间太少，就等下次
		if delta_quota < 1:
			return
		# 增加剩余空间
		self.left_quota += delta_quota
		# 记录漏水时间
		self.leaking_ts = now_ts
		# 剩余空间不得大于容量
		if self.left_quota > self.capacity:
			self.left_quota = self.capacity

	# 判断是否能灌水
	def watering(self,quota):
		self.make_space()
		if self.left_quota >= quota:
			self.left_quota -= quota
			return True
		return False

# 所有的漏斗
funnels = {}

'''
判断是否能还能进行操作
capacity:漏斗容量
leaking_rage:漏嘴流水速率quota/s
'''
def is_action_allowed(user_id,action_key,capacity,leaking_rate):
	key = '%s:%s'%(user_id,action_key)
	funnel = funnels.get(key)
	if not funnel:
		funnel = Funnel(capacity,leaking_rate)
		funnels[key] = funnel
	return funnel.watering(1)

if __name__ == '__main__':
	for i in range(20):
		print(is_action_allowed('ranlay','reply',15,0.5))