#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import socket, time


class SocketHandler():
    def __init__(self, socketClient, address):
        i = 0
        while True:
            data = socketClient.recv(4)
            # sendStr =
            if len(data) <= 0:
                break
            else:
                if "bye" == data:
                    print address, "send to me 'bye' now close this connect"
                    socketClient.send("bye")
                    break
                else:
                    print  data.decode('utf-8')
                    socketClient.send("i have received data:" + data)
                    i += 1
                    print i

            socketClient.close()
def test():
    print "module test"
