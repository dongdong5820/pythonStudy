# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/8/3 13:47
desc: socket网络编程，tcp服务器端编程。接受多个客户端
"""
import socket
# 创建socket
tcpSerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定的ip和port
address = ("", 7788)
# 绑定ip和port
tcpSerSocket.bind(address)
# 监听
tcpSerSocket.listen(5)

while True:
    # 接受客户端
    newSocket, clientAddr = tcpSerSocket.accept()
    print('接收到客户端:%s:%s'%(clientAddr[0],clientAddr[1]))
    # 关闭与该客户端的socket连接
    newSocket.close()

# 关闭监听的socket，不再接受任务客户端的连接
tcpSerSocket.close()

