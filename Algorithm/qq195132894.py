# -*- coding: utf-8 -*-
'''
195132894
入群题：求1<=i<=10**12范围内所有d(i)的和的末12位，d(i)表示i的正约数的和，i为整数
支持3.0，
'''
import datetime


def d(n):
    starttime = datetime.datetime.now()
    s = 0
    m = int(n**0.5)
    for i in range(1,m):
        s = s + (((1+i)*i)//2) + (((1+n//i)*(n//i))//2)
    s = s + (((1+m)*m)//2)
    for i in range(1,m):
        s = s + ((n//i)-2*m+i)*i
    endtime = datetime.datetime.now()
    print u'耗时',(endtime - starttime).seconds
    return int(s)

#print (d(10**12))


#822467033425 357340138978 right


