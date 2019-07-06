# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2019/7/5 17:24
desc: 授权的handler
"""
import urllib2

# 构建一个需要授权的handler，形式如下   username:passwd@ip:port
authproxy_handler = urllib2.ProxyHandler({"http":"username:passewd@114.215.104.49:16816"})
# 构建一个opener对象
opener = urllib2.build_opener(authproxy_handler)
# 构建请求
request = urllib2.Request("http://www.baidu.com")
# 发送请求获取相应
response = opener.open(request)

# 打印内容
print(response.read())