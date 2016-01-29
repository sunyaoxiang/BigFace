#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
问第4个人岁数，他说比第3个人大2岁。
问第三个人，又说比第2人大两岁。
问第2个人，说比第一个人大两岁。
最后问第一个人，他说是10岁。请问第五个人多大？
@author: sunyx
'''

def howold(n):
    i = 10
    if n == 1:
        return i
    for j in range(0,n-1):
        i = i + 2
    return i
print howold(input('请输入第几'))