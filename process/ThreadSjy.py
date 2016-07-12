#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
from time import sleep, time
import threading


def music(musicName):
    for i in range(3):

        print i, "now  Music ", musicName, '  ', threading.currentThread().getName(), "\n"
        sleep(6)


def movive(moiveName):
    for i in range(5):

        print i, 'mow , I\'m movieing ', moiveName, '  ', threading.currentThread().getName(), "\n"
        sleep(10)


if __name__ == "__main__":
    # music("星语心愿")
    # music("忘情水")
    # movive("yu月光宝盒")
    # movive("齐天大圣")

    threadMusic = threading.Thread(target=music, name="cesshi", args=(u"同一首歌",))

    threadMusic2 = threading.Thread(target=movive, name="ces0", args=(u"凤凰传奇0",))

    threadMusic3 = threading.Thread(target=music, name="ces1", args=(u"凤凰传奇1",))

    threadMusic4 = threading.Thread(target=music, name="ces2", args=(u"凤凰传奇2",))

    threadMusic5 = threading.Thread(target=movive, name="ces3", args=(u"凤凰传奇3",))
    #
    threadMusic6 = threading.Thread(target=movive, name="ces4", args=(u"凤凰传奇4",))

    threadMusic.start()
    threadMusic2.start()
    threadMusic3.start()
    # threadMusic4.start()
    # threadMusic5.start()
    # threadMusic6.start()

    threadMusic.join()
    threadMusic2.join()
    threadMusic3.join()
    # threadMusic4.join()
    # threadMusic5.join()
    # threadMusic6.join()
