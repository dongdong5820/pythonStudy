# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/7/14 22:39
desc:线程安全：给线程枷锁
"""
import threading

g_num = 0
total = 2000000

def worker():
    global g_num
    for i in range(total):
        # 加锁(True代表阻塞方式)
        if mutex.acquire(True):
            g_num += 1
            #执行成功后释放锁
            mutex.release()

if __name__ == '__main__':
    print('线程开始前,g_num is %d' % g_num)
    # 创建一个互斥锁，默认是未上锁状态
    mutex = threading.Lock()
    ths = []
    for i in range(2):
        t = threading.Thread(target=worker)
        t.start()
        ths.append(t)
    # 让主线程等待所有子线程结束
    for t in ths:
        t.join()
    print('线程结束后,g_num is %d' % g_num)