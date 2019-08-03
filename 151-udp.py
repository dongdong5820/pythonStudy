# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/8/3 14:18
desc:socket网络编程，udp收发消息
"""
import socket

# 创建socket
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 目标IP和端口
sendAddr = ('192.168.10.1', 8080)

# 发送消息
udpSocket.sendto(b'this is a message.', sendAddr)

# 接受消息
recvData = udpSocket.recvfrom(1024)
print(recvData)

# 关闭socket
udpSocket.close()

