#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
@author: sunyx
'''

a = [2,3,5,8,9,4]
b = [2,3,8,9,4]

def count1(a,b): #先排序，后逐一对比
    list.sort(a)
    list.sort(b)
    for i in range(0,len(b)):
            if a[i] != b[i]:
                rs = a[i]
                break
    return rs;

#print count1(a,b)
def sumforlist(n): #list内部求和
    s =0
    for i in range(0,len(n)):
        s = s + n[i]
    return s

def count2(a,b): #list内部和相加后直接互减
    rs = abs(sumforlist(a) - sumforlist(b))
    return rs

#print count2(a,b)

def count3(a,b): #分别计算a的单个元素在b中有几个，为0的即为多余的
    for i in range(0,len(a)):
        if b.count(i) == 0 :
            rs = i
    return rs

#print count3(a,b)

def count4(a,b): #传统对比法
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            s = 0
            if a[i] == b[j]:
                s += 1
            if s < 1 :
                rs = a[i]
    return rs

#print count4(a,b)
