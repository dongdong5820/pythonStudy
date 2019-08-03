# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/8/3 13:47
desc: socket网络编程，udp绑定固定端口
"""
import socket

# 创建socket
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定固定IP和端口
bindAddr = ("",53727)

# 绑定IP和端口
udpSocket.bind(bindAddr)

# 接受消息
recvData = udpSocket.recvfrom(1024)
print(recvData)

# 关闭socket连接
udpSocket.close()

