# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/8/3 13:47
desc: socket网络编程，tcp服务器端编程
    1.socket创建一个套接字
    2.bind绑定ip和port
    3.listen使套接字变为可以被动连接
    4.accept等待客户端连接
    5.recv/send接受发送数据
"""
from socket import *
# 创建socket
tcpSerSocket = socket(AF_INET, SOCK_STREAM)
# 绑定的ip和port
address = ("", 7788)
# 绑定ip和port
tcpSerSocket.bind(address)
# 使用socket创建的套接字默认是主动的，使用listen使其变为被动，这样就可以接受数据
tcpSerSocket.listen(5)
# 如果有新的客户端来连接服务器，那么就产生一个新的套接字专门为这个客户端服务 clientAddr客户端的ip和port
newSocket, clientAddr = tcpSerSocket.accept()
# 接受对方发送的数据，最大1024个字节
recvData = newSocket.recv(1024)
print('接收到的数据为：%s'%recvData)
# 发送一条数据给客户端
newSocket.send(b"Thank you !")
# 关闭这个新的套接字。不再为这个客户端服务
newSocket.close()
# 关闭监听套接字。整个程序不再接受任何新的客户端连接
tcpSerSocket.close()
