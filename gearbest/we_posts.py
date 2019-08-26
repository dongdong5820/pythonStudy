# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2019/7/5 17:37
desc: 通过cookiejar保存登录会话信息
	1、先爬登录页面 https://loginm.gearbest.net/m-users-a-sign.htm?type=1, 获取登录POST所需要的参数_token
	2、根据用户输入的用户名和密码，提交登录POST请求，https://loginm.gearbest.com/user/login。 登录成功后会保存会话信息
	3、访问需要登录后的请求.（社区帖子点赞/取消点赞，浏览，转发）
"""
import urllib
import urllib2
# 处理会话cookie的库
import cookielib
# 解析字符串为HTML DOM的库(需要先安装)
from lxml import etree
import time,sys

# 登录界面url
login_url = 'https://loginm.gearbest.com/m-users-a-sign.htm?type=1'
# 登录post的url
login_post_url = 'https://loginm.gearbest.com/user/login'
# 帖子操作url
we_posts_url = 'https://m.gearbest.com/we/posts/'

# 通过cookieJar()类构建一个cookieJar对象，用来保存cookie的值
cookie = cookielib.CookieJar()
# 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie。参数就是构建的CookieJar对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
# 创建一个opener对象
opener = urllib2.build_opener(cookie_handler)
# 通过自定义opener的addheaders参数，添加HTTP报头
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")]
# 构建请求
request = urllib2.Request(login_url)
# 发送请求，并获取相应
html = opener.open(request).read()
# 解析HTML文档字符串为HTML DOM模型
content = etree.HTML(html)
# xpath返回所有匹配成功的集合列表(获取_token)
_token = (content.xpath('//meta[@name="csrf-token"]')[0]).get('content')

formdata = {
	"email":"suchangdong@globalegrow.com",
	"passWord":"123456",
	"timeZone":"+8",
	"userCenterSuffix":"",
	"_token":_token
}
data = urllib.urlencode(formdata)
# 构建登录POST请求
request = urllib2.Request(login_post_url, data = data)
# 发送请求,登录成功
opener.open(request).read()
# 构建浏览帖子请求
posts_id = 226
formdata = {
    'posts_id':posts_id
}
data = urllib.urlencode(formdata)
# 构建点赞帖子请求
request = urllib2.Request(we_posts_url + 'like', data = data)
html = opener.open(request).read()
print('like: '+ html)
# 构建浏览帖子请求
request = urllib2.Request(we_posts_url + 'read', data = data)
html = opener.open(request).read()
print('read:' + html)
# 构建转发帖子请求
request = urllib2.Request(we_posts_url + 'forward', data = data)
html = opener.open(request).read()
print('forward:' + html)



