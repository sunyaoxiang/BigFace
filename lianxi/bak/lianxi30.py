#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
一个5位数，判断它是不是回文数。
即12321是回文数，个位与万位相同，十位与千位相同。
@author: sunyx
'''
def ishuiwen(n):
    l = []
    for i in range(5,0,-1):
        t = n // (10 ** (i-1))
        #print i,10 ** (i-1)
        n = n - t * (10 ** (i-1))
        #print t,n
        l.append(t)
    for j in range(0,3):
        if l[j] == l [-j-1]:
            ishuiwen = True
        else:
            ishuiwen = False
            break
    return ishuiwen
        
#print ishuiwen(input('输入1个5位数'))
s = 0
for i in range(10000,100000):
    if ishuiwen(i) == True:
        s += 1
        print i,'是回文'
print '总共',s,'个回文'