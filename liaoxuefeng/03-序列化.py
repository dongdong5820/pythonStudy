#!/usr/bin/env python
#coding:utf-8

print('-'*20 + 'stringIO')
from io import StringIO
# 写入stringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())
# 用str初始化StringIO
f = StringIO('Hello!\nHi!\nWorld!')
while True:
    s = f.readline()
    if s == '':
        break;
    print(s.strip())

print('-'*20 + 'BytesIO')
from io import BytesIO
f = BytesIO()
f.write('中文,北京你好！'.encode('utf-8'))
print(f.getvalue())
# 用二进制初始化BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

d = dict(name='jase', age=12, score=85)

print('-'*20 + 'pickle序列化')
import pickle
bys = pickle.dumps(d)
print(bys)
ed = pickle.loads(bys)
print(ed)

print('-'*20 + 'json序列化')
import json
# json.dumps()将python对象转换成json字符串
# json.loads()将json字符串转换成python对象
ej = json.dumps(d)
print('类型:%s,值:%s'%(type(ej), ej))
dj = json.loads(ej)
print('类型:%s,值:%s'%(type(dj), dj))
