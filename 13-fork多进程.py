# coding=utf-8
import os,time

pid = os.fork()
num = 100
if pid < 0:
	print('fork调用失败')
elif pid == 0 :
	time.sleep(2)  #休眠2秒
	num += 1
	print('我是子进程pid:%d, 我的父进程pid:%d, num:%d'%(os.getpid(), os.getppid(), num))
else:
	time.sleep(3)
	print('我是父进程pid:%d, 我的子进程pid:%d, num:%d'%(os.getpid(),pid, num))

print('父子进程都可以执行这里的代码')
