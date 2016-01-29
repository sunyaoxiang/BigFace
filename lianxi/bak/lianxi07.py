#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
将一个列表的数据复制到另一个列表中。
@author: sunyx
'''

list1 = [1,2,3]
list2 =[]

def copytolist1(list1,list2):
    for i in list1:
        list2.append(i)
    return list2

#print copytolist1(list1,list2)

def copytolist2(list1,list2):
    list2 = list1[:]
    return list2

print copytolist2(list1,list2)