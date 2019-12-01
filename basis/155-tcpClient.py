# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/8/3 13:47
desc: socket网络编程，tcp客户端编程
    1.socket创建一个套接字
    2.连接服务器端
    3.recv/send接受发送数据
"""
from socket import *
# 创建socket
clientSocket = socket(AF_INET, SOCK_STREAM)
# 服务器ip和port
serverAddr = ("192.168.10.63", 7788)
# 连接服务器
clientSocket.connect(serverAddr)
# 发送数据
clientSocket.send(b"hello")
# 接受数据
recvData = clientSocket.recv(1024)
print(recvData)

# 关闭socket
clientSocket.close()
