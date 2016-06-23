#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunjiyun'
import os
print os.name
# print os.uname()  windows 不提供 linux 等提供
print os.environ
print os.getenv("path")
print os.getenv("JAVA_HOME")
print os.path.realpath
print os.path.abspath(".")