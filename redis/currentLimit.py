# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2020/5/8 15:44
desc: redis实现简单限流(时间窗口)
"""
import redis
import time
from mySentinel import *

# 主库实例
master = get_master()
slave = get_slave()
print(master,slave);

'''
限流函数，如同一用户的同一行为在period时间内最多操作max_count次
'''
def is_action_allowed(user_id,action_key,period,max_count):
	key = 'hist:%s:%s'%(user_id,action_key)
	# 毫秒时间戳
	now_ts = int(time.time()*1000)
	# 管道操作
	with master.pipeline() as pipe:
		# 记录行为
		pipe.zadd(key, {now_ts:now_ts})
		# 移除时间窗口之前的行为记录，剩下的都是时间窗口内的
		pipe.zremrangebyscore(key,0,now_ts-period*1000)
		# 获取窗口内的行为数量
		pipe.zcard(key)
		# 设置zset过期时间，避免冷用户长期占用内存
		# 过期时间等于时间窗口的长度，再多宽限1秒
		pipe.expire(key, period+1)
		# 批量执行
		_,_,current_count,_ = pipe.execute()
	# 比较数量是否超标
	return current_count<=max_count

if __name__ == '__main__':
	for i in range(20):
		# 60秒内最多操作5次
		print(is_action_allowed('ranlay','reply',60,5))