#!/usr/bin/env python
#coding:utf-8
import requests, json, time, os, sys
from contextlib import closing

'''
类说明：爬取unsplash.com网站上的50张高清图片到本地
'''
class getPhotos(object):
	def __init__(self):
		self.photoIds = []
		self.downloadServer = 'http://unsplash.com/photos/xxx/download?force=true'
		self.target = 'http://unsplash.com/napi/photos?page=%d&per_page=10'
		self.headers = {'Referer':'https://unsplash.com/', 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
	
	'''
	函数说明：获取图片的ID
	Parameters:
		无
	Returns:
		无
	'''
	def getPhotoIds(self):
		for i in range(5):
			target = str.format(self.target%(i+1))
			req = requests.get(url=target, headers=self.headers, verify=False)
			html = json.loads(req.text)
			for each in html:
				self.photoIds.append(each['id'])
			time.sleep(1)

	'''
	函数说明：下载图片到本地文件
	Parameters:
		photoId - 图片id
		filename - 本地文件
	Returns:
		无
	'''
	def download(self, photoId, filename):
		target = self.downloadServer.replace('xxx',photoId)
		#req = requests.get(url=target, stream=True, headers=self.headers, verify=False)
		#print(req.raw) <urllib3.response.HTTPResponse object at 0x7f1dfe22c6a0> HTTPResponse对象
		with closing(requests.get(url=target, stream=True, headers=self.headers, verify=False)) as r:
			# 以二级制追加写的方式打开文件
			with open(filename, 'ab+') as f:
				#以iter_content()模式将资源流保存到文件
				for chunk in r.iter_content(chunk_size=1024):
					if chunk:
						f.write(chunk)
						f.flush()

if __name__ == '__main__':
	gp = getPhotos()
	print('获取图片连接中...')
	gp.getPhotoIds()
	#当前文件的父级目录下的/storage/images/目录
	dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + '/storage/images/'
	#目录是否存在,不存在则创建目录
	if not os.path.exists(dir):
		os.mkdir(dir)
	print('图片下载中...')	
	for i in range(len(gp.photoIds)):
		filename = os.path.join(dir, str(i+1) + '.jpg')
		print('  正在下载第%d张图片...'%(i+1))
		gp.download(gp.photoIds[i], filename)
	print('图片下载完成！')
