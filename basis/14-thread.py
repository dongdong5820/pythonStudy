# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/7/14 21:22
desc:线程使用
"""
import threading,time

def worker(num):
    print('线程执行%d'%num)
    time.sleep(2)

if __name__ == '__main__':
    for x in range(5):
        # 创建线程
        t = threading.Thread(target=worker, args=(x+1,))
        #执行线程
        t.start()
    print('主线程结束')