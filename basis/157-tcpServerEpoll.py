# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/8/3 13:47
desc: socket网络编程，tcp服务器端编程。epoll方式
"""
import socket
import select
import sys

# 创建socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置socket选项  SOL_SOCKET正在使用的socket，SO_REUSEADDR表示关闭该socket后操作系统是否立刻释放该socket端口.1表示立刻释放，0表示过几分钟才释放
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
address = ("", 7788)
# 绑定ip和port
serverSocket.bind(address)
# 监听
serverSocket.listen(5)
# 创建epoll
epoll = select.epoll()
# 向epoll注册设备(socket，键盘输入)
epoll.register(serverSocket.fileno(), select.EPOLLIN|select.EPOLLET)
epoll.register(sys.stdin.fileno(), select.EPOLLIN|select.EPOLLET)
# 所有socket连接字典
connections = {}
# 所有客户端ip和port字典
clientAddrs = {}

while True:
    running = True
    # 使用epoll去查看每个设备的状态，将有事件发生的设备放入里诶包
    pollList = epoll.poll()
    # fd文件描述符，event事件
    for fd,event in pollList:
        if fd == serverSocket.fileno():
            # 处理服务器(接受客户端连接)
            newSocket,clientAddr = serverSocket.accept()
            print('接受新客户端连接：%s:%s'%(clientAddr[0], clientAddr[1]))
            connections[newSocket.fileno()] = newSocket
            clientAddrs[newSocket.fileno()] = clientAddr
            epoll.register(newSocket.fileno(), select.EPOLLIN|select.EPOLLET)
        elif fd == sys.stdin.fileno():
            # 处理用户键盘输入
            cmd = sys.stdin.readline()
            running = False
            break
        else:
            # 处理客户端socket
            recvData = connections[fd].recv(1024)
            if recvData:
                print('接受到消息：%s'%recvData)
                # 回传客户端消息
                connections[fd].send(b'epoll:' + recvData)
            else:
                connections[fd].close()
                print('客户端：%s:%s关闭'%(clientAddrs[fd][0],clientAddrs[fd][1]))
                epoll.unregister(fd)

    if running == False:
        break

# 关闭socket
serverSocket.close()
