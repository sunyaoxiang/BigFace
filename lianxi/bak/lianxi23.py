#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
题目：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
@author: sunyx
'''
def print1(n):
    for i in range(0,n):
        t = abs(i - n //2)
        #print t
        print ' '*t,'*'*(n-2*t),' '*t
        
print1(input('输入菱形上下限'))