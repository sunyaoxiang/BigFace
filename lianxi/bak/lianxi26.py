#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
利用递归方法求5!。
@author: sunyx
'''
def qjc(n):
    t = 1
    for n in range(1,n+1):
        t *= n
    return t


def qjcx(m):
    for i in range(1,m+1):
        print i,'!',qjc(i)
        
qjcx(8)