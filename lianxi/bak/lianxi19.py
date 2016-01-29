#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。
@author: sunyx
'''
def fenjie(n):
    k = n
    l = [1]
    for i in range(2,n):
        if n % i == 0:
            l.append(i)
    #print l,reduce(lambda x,y : x+y,l)
    #return reduce(lambda x,y : x+y,l)
    if k == reduce(lambda x,y : x+y,l):
        #print k,'是完数'
        return True
    else:
        #print k,'不是完数'
        return False
    
#fenjie(input('输入1个数'))

ws = []
for i in range(2,1001):
    if fenjie(i) == True:
        #print i,'是完数'
        ws.append(i)
    #else:
        #print i,'不是完数'
print ws
