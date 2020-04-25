# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2020/4/23 17:05
desc: 哨兵操作
"""
from redis.sentinel import Sentinel

# 哨兵节点
mySentienlAddr = [('192.168.10.10',27310),('192.168.10.10',27311),('192.168.10.10',27312)]
# 哨兵监听主节点名称
mySentinelName = 'sentinel-192.168.10.10-7310'
sentinel = Sentinel(mySentienlAddr, socket_timeout=2000)
# discover_xx 方法发现主从地址，主只有一个，从可以有多个
master = sentinel.discover_master(mySentinelName)
slaves = sentinel.discover_slaves(mySentinelName)
print(master, slaves)
# xxx_for 方法从连接池中拿出一个连接，获取主从实例
master = sentinel.master_for(mySentinelName, socket_timeout=2000, decode_responses=True)
slave = sentinel.slave_for(mySentinelName, socket_timeout=2000, decode_responses=True)
print(master,slave)
master.set('foo','bar')
print(slave.get('foo'))
print(type(slave.get('foo')))