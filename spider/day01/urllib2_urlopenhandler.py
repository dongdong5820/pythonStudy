# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2019/7/5 16:57
desc: handler处理
"""
import urllib2

# 构建一个HTTPHandler处理对象，用户处理Http请求. 增加参数debuglevel=1将自动打开debug log模式，程序在执行的时候会打印收发包的信息
http_handler = urllib2.HTTPHandler(debuglevel=1)
# 调用build_opener()方法构建一个自定义的opener对象，参数是构建的处理器对象
opener = urllib2.build_opener(http_handler)
# 构建请求
request = urllib2.Request('http://www.baidu.com')
# 用户opener对象调用open()方法发送请求，并接受相应内容
response = opener.open(request)
print(response.read())