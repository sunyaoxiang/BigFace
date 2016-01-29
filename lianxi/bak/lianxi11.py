#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，
问每个月的兔子总数为多少？ 
@author: sunyx
'''

def qz1(m):
    if m % 2 != 0:
        n = m //2
    else:
        n = m // 2 +1
    f1 = 1
    f2 = 1
    l = []
    l.append(f1)
    l.append(f2)
    for i in range(1,n+1):
        f1 = f1 + f2
        f2 = f1 + f2
        l.append(f1)
        l.append(f2)
    return l[m-1]

print qz1(8)

'''
f1 = 1
f2 = 1
for i in range(1,21):
    print '%12d %12d' % (f1,f2)
    if (i % 2) == 0:
        print ''
    f1 = f1 + f2
    f2 = f1 + f2
'''