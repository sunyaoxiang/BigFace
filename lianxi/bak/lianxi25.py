#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
求1+2!+3!+...+20!的和。
@author: sunyx
'''
'''
c = 0
for i in range(1,21):
    s = 1
    for j in range(1,i+1):
        s = j*s
        print i,'! = ',s
    print i,c,s
    c = c + s
    
print c
'''
n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    print n,t
    #s += t
#print '1! + 2! + 3! + ... + 20! = %d' % s