#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
from SocketServer import TCPServer,UDPServer
print '多重继承'
class Animal:
    pass
class Bird(Animal):
    pass
class Mammal(Animal):
    pass

class Runnale(object):
    def run(self):
        print 'running'
class Flyable(object):
    def fly(self):
        print 'flyable'
class Dog(Mammal,Runnale):
    def __init__(self):
        print 'i am a dog,i am Mammal i can'
class Parrot(Bird,Flyable):
    def __init__(self):
        print("这是鹦鹉,",self.fly())

if __name__ == "__main__":
    dog = Dog()
    dog.run()
    parrot = Parrot()
    parrot.fly()


class MyTCPServer(TCPServer):
    def __init__(self):
        print 'this is tcpSever'
class MyUDPServer(UDPServer):
    def __init__(self):
        print 'this is UDPSERVER'
if __name__ =="__main__":
    myTcpServer = MyTCPServer()

