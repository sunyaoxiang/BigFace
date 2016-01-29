#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
@author: sunyx
'''
l = [96, 85, 61, 55, 45, 42, 25, 14, 7, 5]

def insertn(l,n):
    for i in range(0,len(l)-2):
        if n >= l[i] and n <= l[i-1]:
            print i,l[i],l[i+1]
            l.insert(i,n)
            break
    if n <= l[-1]:
        l.append(n)
    elif n >= l[0]:
        l.insert(0,n)
    return l

print l
print insertn(l,input('输入要插入的数'))