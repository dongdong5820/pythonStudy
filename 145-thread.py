# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/7/14 22:17
desc:线程 传可变类型的变量(list,dict,set)
"""
import threading,time

my_list = [5,6,7]
def worker1(list):
    for x in range(3):
        list.append(x+1)
    print('***** in worker1, list is %s'%list)

def worker2(list):
    print('***** in worker2, list is %s' % list)

if __name__ == '__main__':
    print('*****线程执行之前, list is %s' %my_list)
    t1 = threading.Thread(target=worker1,args=(my_list,))
    t1.start()
    time.sleep(1)
    t2 = threading.Thread(target=worker2,args=(my_list,))
    t2.start()
    print('***** 线程结束后, list is %s' %my_list)