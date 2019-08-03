# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/8/3 13:47
desc: socket网络编程，udp制作echo服务器
"""
from socket import *

# 创建socket
udpSocket = socket(AF_INET, SOCK_DGRAM)

# 绑定的IP和端口
bindAddr = ("", 9988)

# 绑定IP和端口
udpSocket.bind(bindAddr)

# 计数器
num = 1
while True:
    # 接受消息
    recvData = udpSocket.recvfrom(1024)
    # 将接受到的消息发送给对方 recvData[0]为字符串数据,recvData[1]为IP和端口
    udpSocket.sendto(recvData[0], recvData[1])
    print('已经将接受到的第%s条数据返回给对方，内容为%s'%(num, recvData[0]))
    num += 1

# 关闭socket
udpSocket.close()
