# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/7/14 21:30
desc:threading.enumerate()返回存活的线程列表
"""
import threading,time

def sing():
    for i in range(5):
        print('我正在唱歌...')
        time.sleep(2)

def dance():
    for i in range(5):
        print('我正在跳舞...')
        time.sleep(2)

if __name__ == '__main__':
    st = threading.Thread(target=sing)
    dt = threading.Thread(target=dance)
    st.start()
    dt.start()
    while True:
        length = len(threading.enumerate())
        print('当前线程数量%d'%length)
        if length <= 1:
            break
        time.sleep(0.5)
    print('主线程结束')