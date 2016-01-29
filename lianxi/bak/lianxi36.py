#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
求100之内的素数。
@author: sunyx
'''

def iss(n):
    nis = True
    for i in range(2,n):
        if n % i == 0:
            nis = False
            break
    return nis

def fwss():
    l = []
    for i in range(1,100):
        if iss(i) == True:
            print i
            l.append(i)
    return l

print fwss()