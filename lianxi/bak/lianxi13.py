#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
打印出所有的"水仙花数"，
所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
@author: sunyx
'''
'''
for i in range(100,999):
    x = i //100
    y = (i - x * 100) // 10
    z = (i -x * 100 - y * 10)

    if x**3+y**3+z**3 == i :
        #print x,y,z
        #print x**3,y**3,z**3
        print i
'''

for i in range(100,999):
    x = i // 100
    y = i // 10 % 10
    z = i %10

    if x**3+y**3+z**3 == i :
        print i
        print x,y,z
        print x**3,y**3,z**3
        