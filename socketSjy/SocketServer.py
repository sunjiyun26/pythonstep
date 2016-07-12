#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import socket, threading
from SocketHandler import SocketHandler,test


def serverReceive(sockClient, address):
    pass


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 9999))
# s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(5)
print("waiting for accept")
while 1:
    i = 0
    socketClient, address = s.accept()
    threading.Thread(target=SocketHandler,)
    socketClient.send("welcome")
    print "conennet success from ", address
    print "waiting for receive message"

s.close()
print "closed"


def startThreadSocket():
    pass
