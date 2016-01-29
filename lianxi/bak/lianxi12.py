#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
判断101-200之间有多少个素数，并输出所有素数。
@author: sunyx
'''

h = 0
for i in range(101,201):
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            leap = 0
            break
        else:
            leap = 1;
    if leap == 1:
        print i
        h += 1
        if h % 10 ==0:
            print ''
print 'count:',h