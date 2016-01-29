#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
数字比较
@author: sunyx
'''
def bijiao(m,n):
    if m > n :
        return m,'大于',n
    elif m < n :
        return m,'小于',n
    else:
        return m,'等于',n
    
m = input('请输入m的值')
n = input('请输入n的值')

print bijiao(m,n)