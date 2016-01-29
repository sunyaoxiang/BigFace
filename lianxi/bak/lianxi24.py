#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
@author: sunyx
'''
def qiuhe1():
    a = 1.0
    b = 2.0
    s = b/a
    for i in range(1,20):
        t = b
        b = a + b
        a = t
        #print a,b,b / a
        s = s + b/a
    return s

#print qiuhe1()

def qiuhe2():
    a = 1.0
    b = 2.0
    s = []
    s.append(b/a)
    for i in range(1,20):
        b,a = a+b,b
        s.append(b/a)
    return s

print reduce(lambda x,y : x+ y,qiuhe2())