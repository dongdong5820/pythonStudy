'''
多线程
'''
import time, threading

#新线程执行的代码
def loop():
    print('thread %s is running... in loop'%threading.current_thread().name)
    n = 0 
    while n < 5:
        n = n + 1
        print('thread %s >>> %s'%(threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended in loop'%threading.current_thread().name)


if __name__ == '__main__':
    print('thread %s is running...'%threading.current_thread().name)
    #实例化线程
    t = threading.Thread(target=loop,name='LoopThread')
    #启动线程
    t.start()
    #等待线程结束
    t.join()
    print('thread %s ended'%threading.current_thread().name)
