#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
输出指定格式的日期。
@author: sunyx
'''
import datetime


#print (datetime.date.today().strftime('%d/%m/%Y'))

print datetime.date.today().strftime('%Y-%m-%d')

i = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
print i
j = datetime.date(2015,11,26)
print j

j = j + datetime.timedelta(days = 100)
print j

k = datetime.date.today()
print k.year
print k.month
print k.day
j = j.replace(year = k.year + 1 )
print j

j = j.replace(day = k.day + 1 )
print j