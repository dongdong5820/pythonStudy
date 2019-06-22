'''
进程间的数据通信: Queue, Pipes
'''

from multiprocessing import Process, Queue
import os,time,random

#写数据进程执行的代码
def write(q):
    print('Process to write: %s'%os.getpid())
    for value in ['A', 'B', 'C', 'D']:
        #向队列中写入数据
        print('Put %s to queue..'%value)
        q.put(value)
        time.sleep(random.random())

#读数据进程执行的代码
def read(q):
    print('Process to read: %s'%os.getpid())
    while True:
        #取出队列里面的数据
        value = q.get(True)
        print('Get %s from queue.'%value)

if __name__ == '__main__':
    #父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    #启动子进程pw，写入数据
    pw.start()
    #启动子进程pr，读取数据
    pr.start()
    #等待pw结束
    pw.join()
    #pr进程代码里面是死循环，无法等待其结束，只能前置终止
    pr.terminate()
