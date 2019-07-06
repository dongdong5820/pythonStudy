# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2019/7/5 17:09
desc: 代理proxy handler
"""
import urllib2

# 代理开关，表示是否开启代理
proxy_swith = False
# 构建一个Hander处理器对象，参数是一个dict，包括代理类型(http/https)和代理服务器IP+port
httpproxy_handler = urllib2.ProxyHandler({"http":"117.91.131.54:9999"})
# 构建一个没有代理的Handler处理器对象
nullproxy_handler = urllib2.ProxyHandler({})

if proxy_swith:
	opener = urllib2.build_opener(httpproxy_handler)
else:
	opener = urllib2.build_opener(nullproxy_handler)

# 构建一个全局的opener，之后所有的请求都可以用到urlopen()方法去发送，也附带Handler功能
urllib2.install_opener(opener)

request = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(request)
print(response.read())