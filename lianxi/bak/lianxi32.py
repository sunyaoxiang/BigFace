#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
按相反的顺序输出列表的值。
@author: sunyx
'''
l = ['a',3,4,2,'43']

def fanxu1(l):
    return l[::-1]

#print fanxu1(l)

def fanxu2(l):
    for i in range(len(l)-1,-1,-1):
        print l[i],i
    return l

print fanxu2(l)