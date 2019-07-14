# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/7/14 17:04
desc: 通过自定义类（继承Process类）创建进程
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
        print('（%s）执行结束，耗时%0.2f秒'%(os.getpid(), (e_time-s_time)))

if __name__ == '__main__':
    s_time = time.time()
    print('当前程序进程（%s）'%os.getpid())
    # 实例化MyProcess类，创建子进程
    p1 = MyProcess(2)
    # 对一个不包含target属性的Process类执行start()方法时，就会运行这个类的run()方法
    p1.start()
    p1.join()
    e_time = time.time()
    print('（%s）执行结束，耗时%0.2f'%(os.getpid(), (e_time-s_time)))