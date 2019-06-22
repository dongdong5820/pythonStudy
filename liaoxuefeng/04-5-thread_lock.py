'''
线程锁
多个线程是共享一个内存空间，当多个线程对同一个变量进行修改时，会造成混乱，这时候就需要用到线程锁
'''
import time, threading

#你的银行存款
balance = 0
#实例化一个线程锁
lock = threading.Lock()

def changeIt(n):
    global balance
    balance = balance + n
    balance = balance - n

def runThread(n):
    for i in range(1000000):
        #先要获取该锁
        lock.acquire()
        try:
            #修改
            changeIt(n)
        finally:
            #释放该锁
            lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=runThread, args=(5,))
    t2 = threading.Thread(target=runThread, args=(6,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('最后存款为:%s'%balance)
