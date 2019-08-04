# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/8/3 13:47
desc: socket网络编程，tcp客户端长连接版本
"""
import socket
# 创建socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddr = ("192.168.10.63", 7788)
# 连接服务器
clientSocket.connect(serverAddr)
while True:
    msg = input('>>')
    # 向服务器发送消息
    clientSocket.send(msg.encode())
    # 接受服务器消息
    recvData = clientSocket.recv(1024)
    print('<<%s'%recvData)
    if msg == 'bye':
        break

# 关闭socket连接
clientSocket.close()

