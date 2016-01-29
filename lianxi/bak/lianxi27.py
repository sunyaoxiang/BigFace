#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
@author: sunyx
'''
def fandayin1():
    l =[]
    for i in range(0,5):
        l.append(raw_input('请输入字符'))
    print l[::-1]
    
#fandayin1()