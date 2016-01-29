#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
输出9*9乘法口诀表。
@author: sunyx
'''

def cf1():
    for i in range(9,0,-1):
        for j in range(9,i-1,-1):
            print i,'*',j,'=',i*j
            
def cf2():
    for i in range(1,10):
        for j in range(1,10):
            result = i*j
            print '%d * %d = % -3d' % (i,j,result)
            #print i,'*',j,'=',result
    return ''
print cf2()