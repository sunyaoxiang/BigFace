#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。 
@author: sunyx
'''
l = ['x','y','z']
for i in l:
    for j in l:
        if j != i:
            for k in l:
                if (k != j) and (j != i) and (k !=i):
                    if (i != l[0]) and (k ==l [1]):
                            print i,j,k
            