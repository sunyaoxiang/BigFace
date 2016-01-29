#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
输入某年某月某日，判断这一天是这一年的第几天？
@author: sunyx
'''
year = input("年\n")
month = input("月\n")
day = input("日\n")


months = (0,31,59,90,120,151,181,212,243,273,304,334,365)
if 0<month<=12:
    dayx = months[month -1]
else:
    print '请输入正确的日期'
if (year % 4 ==0) and (year % 400==0) and (year % 100 !=0):
    dayx +=1
dayx += day
print '该日期是',year,'年第',dayx,'天'