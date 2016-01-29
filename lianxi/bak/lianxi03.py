#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？
@author: sunyx
'''

def findx():
    for i in range(0,10000):
        if ((i+100)**0.5)%1 ==0 and ((i+268)**0.5)%1 ==0:
            print i
            
import math
def findx1():
    for i in range(0,10000):
        #print int(math.sqrt(i+100))**2 
        if i+100 == int(math.sqrt(i+100))**2 and i+268 ==int(math.sqrt(i+268))**2:
            print i
        
findx1()