'''
datetime 时间处理模块
'''
from datetime import datetime
print('*' * 20 + 'datetime 时间处理模块')
now = datetime.now()
print('当前时间: %s'%now)
print('当前时间戳:%s'%now.timestamp())
dt = datetime(2019, 6, 20, 19, 32)
print('指定日期和时间：%s'%dt)
print('datetime转换为timestamp时间戳:%s'%dt.timestamp())
t = 1558300806
print('timestamp转换为datetime:%s'%datetime.fromtimestamp(t))
print('timestamp转换为UTC-datetime:%s'%datetime.utcfromtimestamp(t))
str = '2019-5-20 5:20:6'
print('str转换成datetime:%s'%datetime.strptime(str, '%Y-%m-%d %H:%M:%S'))
print('datetime转换成str:%s'%now.strftime('%a,%b %d %H:%M'))

import time
print('当前系统的时区为：%s'%time.strftime('%Z', time.localtime()))
