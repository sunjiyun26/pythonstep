#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import socket
# AF_INET6 是 ipv6
socketsjy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketsjy.connect(("127.0.0.1",9999))
socketsjy.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
bufferSjy = []
# numcount =  socketsjy.
while True:
    data =socketsjy.recv(1024)
    if data:
        bufferSjy.append(data)
        print bufferSjy
    else:
        break
socketsjy.close()