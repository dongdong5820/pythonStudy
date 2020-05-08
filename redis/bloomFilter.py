# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2020/5/8 12:19
desc: 布隆过滤器
docker安装redis:
1)docker pull redislabs/rebloom
2)docker run -p7380:6379 redislabs/rebloom
3)redis-cli -p 7380
"""
import redis
import random

host = '192.168.10.10'
port = 7380
client = redis.Redis(host=host,port=port,decode_responses=True)
print(client)
# 布隆过滤器测试
key = 'codehole';
client.delete(key)

# 测试一
def test1(num):
	for i in range(num):
		client.execute_command('bf.add', key, 'user%d'%i)
		ret = client.execute_command('bf.exists', key, 'user%d'%i)
		if ret == 0:
			print(i)
			break

# 测试二
def test2(num):
	for i in range(num):
		client.execute_command('bf.add', key, 'user%d'%i)
		ret = client.execute_command('bf.exists', key, 'user%d'%(i+1))
		if ret == 1:
			print(i)
			break

# 获取随机数(n个字母组成)
def random_string(n):
	CHARS = ''.join([chr(ord('a') + i) for i in range(26)])
	chars = []
	for i in range(n):
		idx = random.randint(0,len(CHARS)-1)
		chars.append(CHARS[idx])
	return ''.join(chars)

# 测试三
def test3(num):
	users = list(set([random_string(64) for i in range(num)]))
	print('total users:', len(users))
	# 切成两个列表
	pos = int(len(users)/2)
	user_train = users[:pos]
	user_test = users[pos:]
	falses = 0
	for user in user_train:
		client.execute_command('bf.add',key,user)
	print('all trained')
	for user in user_test:
		ret = client.execute_command('bf.exists',key,user)
		if ret == 1:
			falses +=1
	print(falses, len(user_test))

if __name__ == '__main__':
	print('脚本执行开始...')
	# test1(1000)
	# test2(1000)
	test3(100000)
	print('脚本执行结束。')