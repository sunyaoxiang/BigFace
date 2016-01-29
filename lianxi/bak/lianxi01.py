#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
@author: sunyx
'''
a = [1,2,3,4]
s = 0
for i in a:
    for j in a:
        for k in a:
            if (i != j) and (j != k) and (i != k):
                print i*100+j*10+k
                s +=1
print s