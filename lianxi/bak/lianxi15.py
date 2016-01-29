#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
@author: sunyx
'''
def prt(n):
    Level = ''
    if n >= 90:
        Level = 'A'
    else:
        if n >= 60:
            Level = 'B'
        else:
            Level = 'C'
    return Level

#print prt(input('请输入学生成绩'))

def prt2(n):
    r = [60,90]
    rl = ['A','B','C']
    Level = ''
    for i in range(0,len(r)):
        t = r[i]
        #print t
        if n < t:
            Level = rl[-i-1]
            break
        else:
            Level = rl[0]
    return Level
# print prt2(input('请输入学生成绩：'))

def prt3(n):
    if n >= 90:
        Level = 'A'
    elif n < 60:
        Level = 'C'
    else:
        Level = 'B'
    return Level

#print prt3(input('请输入学生成绩：'))

def prt4(n):
    if n >= 90:
        Level = 'A'
    elif n >= 60:
        Level = 'B'
    else:
        Level = 'C'
    return Level

print prt4(input('请输入学生成绩：'))