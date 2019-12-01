#!/usr/bin/env python
#coding:utf-8

import os,sys

'''
查找当前文件，目录及其子目录中含有hello的以.py结尾的所有文件
'''

fileList = []
#递归函数，函数中所有的文件路径全部采用绝对路径。parentDir:文件所在父目录的绝对路径，fileName:当前处理的文件或目录
def findHello(parentDir, fileName):
	#正在处理的文件或目录的绝对路径
	fileAbsPath = os.path.join(parentDir,fileName)
	#如果是一个目录，列出该目录下的所有文件列表
	if os.path.isdir(fileAbsPath):
		for f in os.listdir(fileAbsPath):
			findHello(fileAbsPath, f)
	else:
		#如果文件以.py结尾，并且内容含有hello
		if fileAbsPath.endswith('.py') and readAndFindHello(fileAbsPath):
			fileList.append(fileAbsPath)
		
#读取py结尾的文件内容中是否含有hello。有返回True，否则返回False
def readAndFindHello(pyFile):
	flag = False
	f = open(pyFile)
	while True:
		#读取其中一行
		line = f.readline()
		if '' == line:
			break
		elif 'hello' in line:
			flag = True
			break
	return flag

#当前文件所在目录(绝对路径)
parentDir = os.path.abspath(os.path.dirname(__file__))
fileName = ''
findHello(parentDir, fileName)
print('含有hello的文件列表：%s'%fileList)
