#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
输入三个整数x,y,z，请把这三个数由小到大输出。
@author: sunyx
'''
'''
x = input("x\n")
y = input("y\n")
z = input("z\n")

def paixu1():
    l = []
    l.append(x)
    l.append(y)
    l.append(z)
    list.sort(l)
    print l
    list.reverse(l)
    print l
    
#paixu1()
'''
def paixu2(x,y,z):
    t = 0
    if x > y:
        t = x
        x = y
        y = t
        print x,y,z
        if y > z:
            t = y
            y = z
            z = t
            print x,y,z
            if x > y:
                t = y
                y = x
                x = t
                print x,y,z
    else:
        if y > z:
            t = y
            y = z
            z = t
            #print '21:',x,y,z
            if x > y:
                t = y
                y = x
                x = t
                #print x,y,z
    return x,y,z

#print paixu2(x,y,z)


def paixu3():
    l = []
    for i in range(0,3):
        x = input('请输入数字')
        l.append(x)
    l.reverse()
    print l
paixu3()