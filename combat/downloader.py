#coding:utf-8
from bs4 import BeautifulSoup
import requests, sys, os

'''
类说明：下载《笔趣看》网小说《一念永恒》
Parameters:
	无
Returns:
	无
Desc:
	必须先安装requests,beautifulsoup第三方库
	pip3 install requests
	pip3 install beautifulsoup4
'''
class downloader(object):
	def __init__(self):
		self.server = 'http://www.biqukan.com/'
		self.target = 'http://www.biqukan.com/1_1094/'
		self.names = [] #存放章节名
		self.urls = []  #存放章节链接
		self.nums = 0 #章节数量
	
	'''
	函数说明：获取所有下载链接
	'''
	def get_download_url(self):
		req = requests.get(url=self.target)
		html = req.text
		#将文本转换成beautifulsoup对象
		div_bf = BeautifulSoup(html,'html.parser')
		#查找类名为listmain的div，返回一个list
		div = div_bf.find_all('div', class_='listmain')
		#在div中查找所有的a标签,返回一个列表
		a_bf = BeautifulSoup(str(div[0]),'html.parser')
		a = a_bf.find_all('a')
		self.nums = len(a[16:-4]) #序列切片，从15个元素开始取[前面的(最新更新文章，外传篇均去掉)],取到倒数第5个元素截止
		for each in a[16:-4]:
			self.names.append(each.string)
			self.urls.append(self.server + each.get('href'))
	
	'''	
	函数说明：获取章节内容
	Parameters:
		target - 下载链接(string)
	Returns:
		tests - 章节内容(string)
	'''
	def get_contents(self,target):
		req = requests.get(url = target)
		html = req.text
		bf = BeautifulSoup(html,'html.parser')
		#获取类名为showtxt的div的内容，并将8个&nbsp;替换成\n\n
		texts = bf.find_all('div', class_='showtxt')
		if texts:
			texts = texts[0].text.replace('\xa0'*8, '\n\n') 			
		else:
			texts = ''	
		return texts

	'''
	函数说明：将爬取的文章内容写入文件
	Parameters:
		name - 章节名称(string)
		path - 当前路径下，小说保存名称(string)
		text - 章节内容(string)
	Returns:
		无
	'''
	def writer(self, name, path, text):
		with open(path, 'a', encoding='utf-8') as f:
			f.write(name+'\n')
			f.writelines(text)
			f.write('\n\n')

if __name__ == '__main__':
	dl = downloader()
	dl.get_download_url()
	print('《一念永恒》开始下载：')
	#当前文件的父级目录
	dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
	fileName = os.path.join(dir + '/storage/', '1-一念永恒.txt')
	for i in range(dl.nums):
		dl.writer(dl.names[i], fileName, dl.get_contents(dl.urls[i]))
		sys.stdout.write(' 已下载：%.3f%%'%float(i/dl.nums) + '\r') 
		sys.stdout.flush()
	print('《一念永恒》下载完成')
