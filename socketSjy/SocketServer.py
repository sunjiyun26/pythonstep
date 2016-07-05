#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import SocketServer,socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",9999))
s.listen(5)
print("waiting for accept")
while True:
   socket,address = s.accept()
   print address
