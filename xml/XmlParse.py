#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'sunjiyun'
from xml.parsers.expat import ParserCreate


class DefaultHandler(object):
    def start_element(self, name, attribute):
        print "sax start_element123 %s attr %s" % (name, attribute)

    def end_element(self, name):
        print "end element %s" % name

    def char_data(self, data):
        print "node data is %s" % (data)


# parser = ParserCreate()
# parser.
# # parser.
if __name__ == "__main__":
    xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
    myhandler = DefaultHandler()

    parser = ParserCreate()
    assert isinstance(parser,object)
    parser.returns_unicode = True
    parser.StartElementHandler = myhandler.start_element
    parser.EndElementHandler = myhandler.end_element
    parser.CharacterDataHandler = myhandler.char_data
    parser.Parse(xml)
