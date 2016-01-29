#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
将一个数组逆序输出。
@author: sunyx
'''
a = [9,6,5,4,1]

#print a[::-1]
for i in range(len(a)-1,-1,-1):
    print a[i]