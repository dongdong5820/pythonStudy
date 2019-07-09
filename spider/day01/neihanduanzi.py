# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2019/7/6 14:26
desc: 爬取内含段子网里面所有段子(使用正则获取匹配网页内容)
"""
import urllib2
import re
import sys

class DuanziSpider():
	def __init__(self):
		self.page = 1
		self.swith = True
		self.filename = 'duanzi.txt'
		self.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
		}

	def loadPage(self):
		"""
		作用：根据url发送请求，获取服务器响应数据
		:return: string 响应的html数据
		"""
		print('正在下载数据...')
		if self.page == 1:
			url = 'http://www.neihan-8.com/wenzi/'
		else:
			url = 'https://www.neihan-8.com/wenzi/index_' + str(self.page) + '.html'
		request = urllib2.Request(url, headers = self.headers)
		# 获取每页的HTML源码字符串
		html = urllib2.urlopen(request).read()
		# 创建正则表达式规则对象，匹配每页的段子内容 re.S表示匹配全部字符串内容
		pattern = re.compile('<div\sclass="desc">(.*?)</div>', re.S)
		# 将正则匹配对象应用到html源码字符串，返回这个页面的所有段子的列表
		content_list = pattern.findall(html)
		# 处理每页段子列表集合
		self.dealPage(content_list)

	def dealPage(self, content_list):
		"""
		作用：使用正则匹配，从页面中获取段子标题和内容
		:param content_list: 每页段子列表集合
		:return: None
		"""
		i = 0
		for item in content_list:
			if i > 0:
				self.writePage(item)
			i += 1

	def writePage(self, item):
		"""
		作用：将段子内容写入文件
		:param item: 段子内容
		:return: None
		"""
		# 写入文件
		print('正在写入数据...')
		with open(self.filename, 'a') as f:
			f.write(item + '\r\n')

	def startWork(self):
		"""
		控制爬虫行为
		:return: None
		"""
		# 循环爬虫，直到self.swith = False
		while self.swith:
			self.loadPage()
			command = raw_input('如果继续，请按回车（退出请输入q）')
			if command == 'q' or command == 'Q':
				self.swith = False
			# 每次循环，页码自增1
			self.page +=1
		print('谢谢使用!')

if __name__ == '__main__':
	DuanziSpider = DuanziSpider()
	DuanziSpider.startWork()