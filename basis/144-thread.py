# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/7/14 22:11
desc:线程 传不可变类型变量
"""
import threading,time

g_num = 100
def worker1(num):
    for x in range(3):
        num += 1
    print('***** in worker1,num is %d'%num)

def worker2(num):
    print('***** in worker2,num is %d' % num)

if __name__ == '__main__':
    print('*****线程执行之前,g_num is %d'%g_num)
    t1 = threading.Thread(target=worker1,args=(g_num,))
    t1.start()
    time.sleep(1)
    t2 = threading.Thread(target=worker2,args=(g_num,))
    t2.start()
    print('*****线程结束之后，g_num is %d'%g_num)