#!/usr/bin/env python
# -*- coding:utf-8 -*-

def log(fun):
    def wrapper(*args,**kw):
        print 'call %s' %fun.__name__
        return fun(*args,**kw)
    return wrapper
@log
def now():
    print '20166-14'
    return '123'
print now()

def log3(text):
    def decorator3(func):
        def wrapper3(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper3
    return decorator3

def log2(text):
    def decorate2(func):
        def wrapperfun(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapperfun
	print '123'
    return decorate2
	
@log2('execute')		
def now2():
    print '12345'
now2()
print now2.__name__
		