#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Process
import os

#子进程要执行的代码
def runProc(name):
    print('Run child process %s (%s)...'%(name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s running...'%os.getpid())
    p = Process(target=runProc, args=('test',))
    print('Child process will start...')
    p.start()
    #父进程等待所有子进程执行完后再执行
    p.join()
    print('Child process end.Parent process id:%s'%os.getpid())
