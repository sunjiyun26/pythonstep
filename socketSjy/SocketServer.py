#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import  socket,threading

def serverReceive(sockClient,address):
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
while True:
    data = socketClient.recv(1024)
    print  "123",data
    # sendStr =
    if len(data) <= 0:
       break
    else:
        if "bye" == data:
            print address, "send to me 'bye' now close this connect"
            socketClient.send("bye")
            break
        else:
            print "not bye", data
            socketClient.send("i have received data:" + data)
            i += 1
            print i

socketClient.close()
s.close()
print "closed"