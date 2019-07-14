# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/7/14 22:01
desc:线程共享全局变量
"""
import threading,time

g_num = 100
def worker1():
    global g_num
    for x in range(3):
        g_num += 1
    print('*****in worker1,g_num is %d'%g_num)

def worker2():
    global g_num
    print('*****in worker2,g_num is %d'%g_num)

if __name__ == '__main__':
    print('*****线程创建之前,g_num is %d'%g_num)
    t1 = threading.Thread(target=worker1)
    t1.start()
    # 休眠一会，保证t1线程执行完
    time.sleep(2)
    t2 = threading.Thread(target=worker2)
    t2.start()
    print('*****线程结束之后，g_num is %d'%g_num)