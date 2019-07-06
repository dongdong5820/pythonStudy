# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2019/7/5 14:38
desc: 发送post请求有道翻译
"""
import urllib,urllib2

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=ugc&sessionFrom=null'
headers = {
	"Accept":"application/json, text/javascript, */*; q=0.01",
	"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
	"X-Requested-With":"XMLHttpRequest"
}
key = raw_input('请输入要翻译的词：')
formdata = {
	"i":key,
	"from":"AUTO",
	"to":"AUTO",
	"smartresult":"dict",
	"client":"fanyideskweb",
	"salt":"15623084910871",
	"sign":"c757e909fcc34e2819479dc251f16aee",
	"ts":"1562308491087",
	"bv":"ab57a166e6a56368c9f95952de6192b5",
	"doctype":"json",
	"version":"2.1",
	"keyfrom":"fanyi.web",
	"action":"FY_BY_REALTlME"
}
# 对提交的参数进行urlencode编码
data = urllib.urlencode(formdata)
# data不能为空时代表post请求
request = urllib2.Request(url, data = data, headers = headers)
print(urllib2.urlopen(request).read())