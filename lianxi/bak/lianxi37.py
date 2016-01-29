#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
对10个数进行排序。
@author: sunyx
'''
l = [5,85,42,61,7,14,25,55,96,45]

'''
#print len(l)
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[i] > l[j]:
            t = l[i]
            l[i] = l[j]
            l[j] = t
            print i+1,j+1,l
print l
'''
s = []
for i in range(0,len(l)):
    s.append(max(l))
    #print s
    del l[l.index(max(l))]
    #print l
print s