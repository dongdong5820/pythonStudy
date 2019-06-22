#!/usr/bin/env python
#coding:utf-8

d = dict(name='jase', age=12, score=85)

print('-'*20 + 'pickle序列化')
import pickle
bys = pickle.dumps(d)
print(bys)
ed = pickle.loads(bys)
print(ed)

print('-'*20 + 'json序列化')
import json
ej = json.dumps(d)
print('类型:%s,值:%s'%(type(ej), ej))
dj = json.loads(ej)
print('类型:%s,值:%s'%(type(dj), dj))
