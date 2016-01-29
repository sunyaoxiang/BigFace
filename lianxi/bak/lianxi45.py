#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
统计 1 到 100 之和。
@author: sunyx
'''

def tj1():
    s = 0
    for i in range(1,101):
        s = s + i
    return s

#print tj1()

def tj2(n,m):
    s = (n+m)*(m-n+1)/2
    return s

#print tj2(0,100)