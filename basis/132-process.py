# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/7/14 16:50
desc: multiprocessing用法
"""
from multiprocessing import Process
import time

def run(title,num,**kwargs):
    time.sleep(2)
    print('子进程：title=%s,num=%s'%(title,num))
    for k,v in kwargs.items():
        print('%s:%s'%(k,v))

if __name__ == '__main__':
    print('父进程')
    p = Process(target=run,name='p1',args=('test', 10,),kwargs={'a':12,'b':'joy'})
    print('子进程即将执行')
    p.start()
    # 等待子进程执行完，里面的1代表等待1秒（配合terminate终止函数）
    p.join(1)
    print('子进程的名称：%s，pid：%d'%(p.name,p.pid))
    # 终止子进程
    p.terminate()
    print('子进程已结束')