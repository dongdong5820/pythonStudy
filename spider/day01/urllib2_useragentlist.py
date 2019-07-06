# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2019/7/5 15:20
desc: 添加use-agent
"""
import urllib2, random

url = 'http://www.baidu.com'

ua_list = [
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
	"Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
	"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
	"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
]
# 在ua列表中随机取一个
user_agent = random.choice(ua_list)
# 构造一个请求
request = urllib2.Request(url)
# add_header() 方法 添加/修改 一个http报头
request.add_header('User-Agent', user_agent)
# get_header() 方法获取请求的报头，注意第一字母大写，其余全是小写
print(request.get_header('User-agent'))