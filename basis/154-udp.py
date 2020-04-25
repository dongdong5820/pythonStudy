# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/8/3 13:47
desc: socket网络编程，udp聊天室
"""
from socket import *
from time import ctime

# 创建socket
udpSocket = socket(AF_INET, SOCK_DGRAM)

# 绑定的IP和端口
bindAddr = ("", 9988)

# 绑定IP和端口
udpSocket.bind(bindAddr)

while True:
    # 接受消息
    recvData = udpSocket.recvfrom(1024)
    # 打印格式化消息
    print('【%s】 %s:%s'%(ctime(), recvData[1][0], recvData[0]))

# 关闭socket
udpSocket.close()
