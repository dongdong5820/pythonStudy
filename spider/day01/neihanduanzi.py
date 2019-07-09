# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2019/7/6 14:26
desc: 爬取内含段子网里面所有段子(使用正则获取匹配网页内容)
"""
import urllib2
import re

class DuanziSpider():
	def __init__(self):
		self.page = 1
		self.swith = True
		self.filename = 'duanzi.txt'

	def loadPage(self,url):
		"""
		作用：根据url发送请求，获取服务器响应数据
		:param url:  q请求url
		:return: string 响应的html数据
		"""
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
		}
		request = urllib2.Request(url, headers = headers)
		html = urllib2.urlopen(request).read()

	def dealPage(self, html):
		"""
		作用：使用正则匹配，从页面中获取段子标题和内容
		:param html:
		:return:
		"""

	def writePage(self):
		pass

	def startWork(self):
		pass

if __name__ == '__main__':
	DuanziSpider = DuanziSpider()
	DuanziSpider.startWork()