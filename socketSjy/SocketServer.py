#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import socket, threading
from SocketHandler import SocketHandler,test
from SocketReceive import recv_end


def serverReceive(sockClient, address):
    pass

def startThreadSocket(socketClient,address):
    receiveMessage = recv_end(socketClient)
    print  receiveMessage,"sever"
    i = 0
    while True:
            data = socketClient.recv(1024)
            # sendStr =
            if len(data) <= 0:
                break
            else:
                if "bye" == data:
                    print address, "send to me 'bye' now close this connect"
                    socketClient.send("bye")
                    socketClient.close()
                    break
                else:
                    print  data.decode('utf-8')
                    socketClient.send("i have received data:" + data)
                    i += 1
                    print i




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 9999))
# s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(5)
print("waiting for accept")
while 1:
    i = 0
    socketClient, address = s.accept()
    clientThread = threading.Thread(target=startThreadSocket,args=(socketClient,address))
    clientThread.start()
    socketClient.send("welcome,you have connect to me")
    print " client conennet success from ", address
    print "waiting for receive message from ",address

s.close()
print "closed"



