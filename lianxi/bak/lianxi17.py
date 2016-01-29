#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
@author: sunyx
'''
s1 = raw_input('请输入一行字符:')

print s1
letters = 0
space = 0
digit = 0
others = 0
for c in s1:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1

print letters,space,digit,others