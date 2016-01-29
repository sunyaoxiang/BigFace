#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
一球从100米高度自由落下，
每次落地后反跳回原高度的一半；再落下，
求它在第10次落地时，共经过多少米？第10次反弹多高？
@author: sunyx
'''
x = 100
l = x
for i in range(1,10):
    x = x * 0.5
    l = l + 2 * x
print l

x = 100
l = x
for i in range(1,11):
    x = x * 0.5
    l = l + 2 * x
print x