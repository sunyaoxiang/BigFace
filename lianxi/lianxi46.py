#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
求输入数字的平方，如果平方运算后小于 50 则退出。
@author: sunyx
'''

def pf1(isgo):
    if isgo != False:
        n = float(raw_input('请输入数字'))
        m = n**2
        if n >= 50:
            print n,'的平方是',m
            isgo = True
            pf1(isgo)
        else:
            isgo = False
            pf1(isgo)
    else:
        print '输入的数字小于 50，程序将停止运行。'


pf1(isgo = True)