# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/7/14 18:28
desc:利用消息队列Queue使多个进程共享数据
"""
from multiprocessing import Process, Queue
import os,time,random

def write(q):
    """
    作用：往队列中写数据
    :param q: 队列
    :return: None
    """
    for item in 'ABC':
        print('正在往队列中写入%s'%item)
        q.put(item)
        time.sleep(random.random())

def reader(q):
    """
    作用：读取队列中的数据
    :param q:队列
    :return: None
    """
    while True:
        if not q.empty():
            item = q.get()
            print('从消息队列读出%s'%item)
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':
    # 创建消息队列
    q = Queue()
    # 创建写入进程
    pw = Process(target=write,args=(q,))
    pw.start()
    pw.join()
    # 创建读进程
    pr = Process(target=reader,args=(q,))
    pr.start()
    pr.join()
    print('所有数据已读完')