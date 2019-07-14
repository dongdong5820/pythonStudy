# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/7/14 22:27
desc:线程不安全
"""
import threading

g_num = 0
"""
当total较小(20),g_num返回的值正常为20+20=40，
当total较大（20000000），g_num返回的值不一定为total的2倍，跟cpu的调度有关
"""
# total = 20
total = 20000000
def worker():
    global  g_num
    for i in range(total):
        g_num += 1

if __name__ == '__main__':
    print('线程开始前,g_num is %d'%g_num)
    for x in range(2):
        t = threading.Thread(target=worker)
        t.start()
    print('线程结束后，g_num is %d'%g_num)