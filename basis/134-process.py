# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/7/14 17:23
desc: 通过自定义类创建多个子进程
"""
from multiprocessing import Process
import time,os

class MyProcess(Process):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        """
        作用：重写Process类的run()方法
        :return: None
        """
        s_time = time.time()
        print('子进程（%s）开始执行，父进程（%s）'%(os.getpid(), os.getppid()))
        time.sleep(self.interval)
        e_time = time.time()
        print('子进程（%s）执行结束，耗时%0.2f'%(os.getpid(), (e_time-s_time)))

if __name__ == '__main__':
    s_time = time.time()
    print('当前程序进程（%s）'%os.getpid())
    # 用于保存所有子进程实例
    childs = []
    for i in range(5):
        p = MyProcess((i+1))
        p.start()
        childs.append(p)
    # 父进程等待所有子进程结束
    for p in childs:
        p.join()
    e_time = time.time()
    print('父进程（%s）执行结束，耗时%0.2f'%(os.getpid(), (e_time-s_time)))