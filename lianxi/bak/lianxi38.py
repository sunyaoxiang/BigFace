#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
求一个3*3矩阵对角线元素之和。
@author: sunyx
'''
l = [[3,4,6],[3,5,2],[6,2,9]]
s = 0
for i in range(0,len(l)):
    s = s + l[i][i]
    
print s