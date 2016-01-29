#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，
几个数相加有键盘控制。
@author: sunyx
'''

def qh1(a,n):
    l = []
    t = a
    l.append(t)
    s = t
    for i in range(1,n):
        t = t + a * 10 ** i
        s = s + t
        l.append(t)
        #print l,s
    return l,s
        

print reduce(lambda x,y : x+y,qh1(2,5)[0])

#print 2 + 22 + 222 + 2222 + 22222

def qh2():
    Tn = 0
    Sn = []
    n = int(raw_input('n = :\n'))
    a = int(raw_input('a = :\n'))
    for count in range(n):
        Tn = Tn + a
        a = a * 10
        Sn.append(Tn)
        print Tn

    Sn = reduce(lambda x,y : x + y,Sn)
    print Sn

#qh2()