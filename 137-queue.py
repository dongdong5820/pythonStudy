# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/7/14 20:58
desc:队列Queue，进程池Pool的使用
"""
from multiprocessing import Pool,Manager
import os,time,random

def write(q):
    """
    作用:向队列中写入数据
    :param q: 消息队列
    :return: None
    """
    for item in 'ABC':
        print('进程（%d）正在写入数据%s'%(os.getpid(), item))
        q.put(item)
        time.sleep(random.random())

def reader(q):
    """
    作用:读取队列中的数据
    :param q: 消息队列
    :return: None
    """
    while True:
        if not q.empty():
            item = q.get()
            print('进程（%d）正在读取数据%s'%(os.getpid(), item))
        else:
            break

if __name__ == "__main__":
    # 创建队列
    q = Manager().Queue()
    # 创建进程池
    pool = Pool(3)
    # 往队列中写入数据进程
    pool.apply(write,args=(q,))
    # 读取队列中的数据进程
    pool.apply(reader,args=(q,))
    # 关闭进程池
    pool.close()
    # 父进程阻塞，等待进程池执行完成
    pool.join()
    print('所有数据已读取完成')