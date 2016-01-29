#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
两个变量值互换。
@author: sunyx
'''
def exchange(a,b):
    a,b = b,a
    return a,b


x = 3
y = 4
x,y = exchange(x,y)
print x,y