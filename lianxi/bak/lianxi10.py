#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
暂停一秒输出。
@author: sunyx
'''
import time

def dum1(n):
    for i in range(0,n):
        #print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        time.sleep(1)

dum1(5)