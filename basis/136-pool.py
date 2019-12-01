# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/7/14 17:58
desc: 进程池Pool
"""
from multiprocessing import Pool
import time,os

def worker(msg):
    s_time = time.time()
    print('子进程（%s）'%os.getpid())
    time.sleep(2)
    e_time = time.time()
    print('子进程msg:%s结束，耗时%0.2f秒'%(msg, (e_time-s_time)))

if __name__ == '__main__':
    s_time = time.time()
    print('父进程（%s）'%os.getpid())
    #实例化进程池（3：代表进程的最大个数）
    pool = Pool(3)

    for x in range(10):
        # 阻塞方式（同步）调用函数
        # pool.apply(worker, args=(x,))
        # 非阻塞（异步）调用函数
        pool.apply_async(worker, args=(x,))
    # 关闭进程池
    pool.close()
    # 主进程等待进程池中所有子进程结束(进程池的join()方法必须在close()方法后面)
    pool.join()
    e_time = time.time()
    print('父进程（%s）结束，耗时%0.2f秒'%(os.getpid(), (e_time-s_time)))
