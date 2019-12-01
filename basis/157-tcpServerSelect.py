# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/8/3 13:47
desc: socket网络编程，tcp服务器端编程。select轮询方式
    select 多路复用
    设备操作也是一种文件操作

    三种标准的输入输出：stdin,stdout,stderr
    socket的收发数据也可以看成是文件的读写
"""
import socket
import select
import sys

# 创建socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置socket选项  SOL_SOCKET正在使用的socket，SO_REUSEADDR表示关闭该socket后操作系统是否立刻释放该socket端口.1表示立刻释放，0表示过几分钟才释放
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
address = ("", 7788)
serverSocket.bind(address)
serverSocket.listen(5)
inputList = [serverSocket,sys.stdin]
while True:
    running = True
    # 使用select查看每个设备的状态，并根据状态将设备放入不同的列表
    readable,writeable,exceptionable = select.select(inputList, [],[])
    # 处理readable设备
    for sock in readable:
        if sock == serverSocket:
			# 处理服务器(接受客户端连接)
            newSocket, clientAddr = sock.accept()
            print('接受到新连接：%s:%s'%(clientAddr[0], clientAddr[1]))
            inputList.append(newSocket)
        elif sock == sys.stdin:
			# 处理用户键盘输入
            cmd = sys.stdin.readline()
            running = False
            break
        else:
			# 处理客户端socket
            # 接受客户端消息
            recvData = sock.recv(1024)
            if recvData:
                print('接受消息：%s'%recvData)
                sock.send(b'select:' + recvData)
            else:
				# 客户端socket已经断开
                sock.close()
                inputList.remove(sock)
    if running == False:
        break

#  关闭socket
serverSocket.close()
