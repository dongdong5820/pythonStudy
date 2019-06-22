'''
线程锁
多个线程是共享一个内存空间，当多个线程对同一个变量进行修改时，会造成混乱
'''
import time, threading

#你的银行存款
balance = 0

def changeIt(n):
    global balance
    balance = balance + n
    balance = balance - n

def runThread(n):
    for i in range(1000000):
        changeIt(n)

if __name__ == '__main__':
    t1 = threading.Thread(target=runThread, args=(5,))
    t2 = threading.Thread(target=runThread, args=(6,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('最后存款为:%s'%balance)
