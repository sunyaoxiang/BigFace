#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
@author: sunyx
'''

def chaishu(n):
    for i in range(0,10):
        if n / (10**i) < 1:
            print i
            break
            
    for j in range(i,0,-1):
        print n // (10**(j-1))
        n = n - (10**(j-1))*(n // (10**(j-1)))
    
chaishu(input('请输入1个不多于5位的整数：'))