# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/7/14 16:28
desc: multiprocessing 创建多个进程
"""
import os,time
from multiprocessing import Process

def run_process(name):
    time.sleep(2)
    print('子进程运行中,name=%s,pid=%d...'%(name, os.getpid()))

if __name__ == '__main__':
    print('父进程:%d', os.getpid())
    # 创建子进程
    p = Process(target=run_process, args=('test',))
    print('子进程即将要执行')
    # 开始执行子进程
    p.start()
    # 父进程等待子进程执行完
    p.join()
    print('子进程已结束')