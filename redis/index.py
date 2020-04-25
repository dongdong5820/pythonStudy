# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2020/4/23 15:20
desc: 操作redis
查看是否安装redis包  pip list
安装redis包 pip install redis
"""
import redis

host = '192.168.10.10'
port = 7310
# redis连接
# decode_responses为True时，写入的value为str类型，否则为字节类型
'''
client = redis.Redis(host=host,port=port,decode_responses=True)
client.set('name','shixiaolong')
client.set('age',10)
print(client.get('name'))
print(type(client.get('age')))
'''

# 连接池
pool = redis.ConnectionPool(host=host,port=port,decode_responses=True)
r = redis.Redis(connection_pool=pool)
key = 'score'
r.set(key,100)
print(r.get(key))

# string操作
r.mset({'k1':'v1', 'k2':'v2'})
print(r.mget(['k1','k2']))
# hash操作
key = 'stars'
r.hset(key, 'liudehua', 40)
r.hset(key, 'linming', 35)
r.hmset(key, {'guofucheng':41,'zhangxueyou':39,'liangchaowei':39})
print(r.hmget(key,['liudehua','zhourunfa']))
print(r.hgetall(key))
print(r.hkeys(key))
#list操作
key = 'fruits'
r.delete(key)
r.lpush(key,'apple','banana','pears')
r.linsert(key,'before','banana','peach')
print(r.lrange(key, 0, -1))
