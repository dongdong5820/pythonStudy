# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/7/14 21:41
desc:自定义类创建线程
"""
import threading
import time


class MyThread(threading.Thread):
    def __init__(self,num,title):
        super().__init__()
        self.num = num
        self.title = title

    def run(self):
        """
        作用:重写threading.Thread类的run()方法，当调用start()方法时执行此方法
        :return:
        """
        for i in range(5):
            print('我是线程%s@%s,num=%s,title=%s'%(self.name,i,self.num,self.title))
            time.sleep(1)

if __name__ == '__main__':
    list = ['a','b','c','d','e']
    for i in range(5):
        # 创建线程
        t = MyThread((i+1), list[i])
        # 执行线程
        t.start()
