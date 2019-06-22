'''
进程池
'''

from multiprocessing import Pool
import os,time,random

def longTimeTask(name):
    print('Run task %s (%s)...'%(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %.2f seconds.'%(name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.'%os.getpid())
    #实例化一个进程池。4表示可以同时跑4个进程
    p = Pool(4)
    for i in range(5):
        #异步执行子进程
        p.apply_async(longTimeTask, args=(i,))
    print('Waiting for all subprocess done...')
    #关闭进程池,此后不能在添加新的process
    p.close()
    #父进程等待所有子进程结束
    p.join()
    print('All subprocess done.')
