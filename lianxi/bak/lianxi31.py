#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
@author: sunyx
'''
dz = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

d1 = raw_input('请输入第一个字母:')

if d1 == 'M':
    print dz[0]
elif d1 == 'W':
    print dz[2]
elif d1 == 'F':
    print dz[4]
elif d1 == 'T':
    d2 = raw_input('请输入第二个字母:')
    if d2 == 'u':
        print dz[1]
    elif d2 == 'h':
        print dz[3]
    else:
        print d1,d2,'输入错误，请重新输入'
elif d1 == 'S':
    d2 = raw_input('请输入第二个字母:')
    if d2 == 'a':
        print dz[5]
    elif d2 == 'u':
        print dz[6]
    else:
        print d1,d2,'输入错误，请重新输入'
else:
    print d1,'输入错误，请重新输入'