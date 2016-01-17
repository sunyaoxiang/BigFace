# -*- coding: utf-8 -*-
'''
195132894
入群题：求1<=i<=10**12范围内所有d(i)的和的末12位，d(i)表示i的正约数的和，i为整数
务必使用Python2.7！
支持3.0，但是结果有偏差
'''
import datetime
starttime = datetime.datetime.now()

def d(n):
    s = 0
    m = int(n**0.5)
    for i in range(1,m):
        s = s + (((1+i)*i)/2) + (((1+n//i)*(n//i))/2)
    #print(i,s)
    s = s + (((1+m)*m)/2)
    for i in range(1,m):
        if ((n//i)-2*m+i > 0):
            s = s + ((n//i)-2*m+i)*i
            #print(i,((n//i)-2*m+i)*i)
        else:
            break;
    return int(s)

print (d(10**12))
endtime = datetime.datetime.now()
print u'耗时',(endtime - starttime).seconds

#822467033425 357340138978 right
#822467033425 357340138978    Python2.7
#822467033425 120044515328    Python3.0
