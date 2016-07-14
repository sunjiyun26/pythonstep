#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import socket,sys
# AF_INET6 是 ipv6
socketsjy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketsjy.connect(("127.0.0.1", 9999))
bufferSjy = []
# numcount =  socketsjy.
while True:
    data = socketsjy.recv(1024)
    print data
    if data != "bye":
        varStr = raw_input()+""
        socketsjy.send(varStr)
    else:
        print "server send me bye"
        socketsjy.close()
        sys.exit(None)

