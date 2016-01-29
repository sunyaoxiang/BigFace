#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
斐波那契数列。
斐波那契数列（Fibonacci sequence），
又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
@author: sunyx
'''
def fib1(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

#print fib1(10)

def fib2(n):
    a,b,t = 1,1,0
    for i in range(n-1):
        t = b
        b = a+b
        a = t
    return a,b

#print fib2(10)

def fib3(n):
    if n == 1 or n == 2:
        return 1
    return fib3(n-1)+fib3(n-2)

#print fib3(10)

def fib4(n):
    if n == 1:
        return [1]
    if n == 2:
        return [2]
    l = [1,1]
    for i in range(2,n):
        l.append(l[-1]+l[-2])
    return l[-1]

print fib4(10)