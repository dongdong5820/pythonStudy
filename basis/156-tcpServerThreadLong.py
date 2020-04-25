# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/8/3 13:47
desc: socket网络编程，tcp服务器端编程。多线程处理长连接
"""
import socket
import threading


def clientProcess(clientSocket):
    """
    作用：线程执行的函数
    :param clientSocket: 与客户端建立连接的socket
    :return: None
    """
    while True:
        # 接受客户端的消息
        recvData = clientSocket.recv(1024)
        print('消息：%s' % recvData)
        # 客户端消息为空时，断开连接
        if len(recvData) <= 0:
            break
        # 给客户端发送消息
        clientSocket.send(recvData)
        if recvData.decode() == 'bye':
            break
    # 关闭此socket连接
    clientSocket.close()

# 创建socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("", 7788)
# 绑定ip和port
serverSocket.bind(address)
# 监听
serverSocket.listen(5)
while True:
    # 与客户端建立socket连接
    newSocket, clientAddr = serverSocket.accept()
    print('接受到客户端连接：%s:%s' % (clientAddr[0], clientAddr[1]))
    # 创建线程
    clientThread = threading.Thread(target=clientProcess, args=(newSocket,))
    # 启动线程
    clientThread.start()

# 关闭监听socket
serverSocket.close()

