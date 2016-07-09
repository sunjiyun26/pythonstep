#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import socket, threading


def serverReceive(sockClient, address):
    pass


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 9999))
# s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(5)
print("waiting for accept")

i = 0
socketClient, address = s.accept()
threading.Thread()
socketClient.send("welcome")
print "conennet success from ", address
print "waiting for receive message"

s.close()
print "closed"
