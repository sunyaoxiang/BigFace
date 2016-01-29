#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''

@author: sunyx
'''
t = 1000 #本金
T = 1400 #充值到账金额
lx = 0.12 #这线利率
fxlx = 0.12 #消费返的利率
fx = 0 #消费返的额度


for i in range(0,12):
    print '第',i+1,'月:'
    print '余额:',T
    mc = input('消费:')
    if T < 0 or T - mc < 0:
        break
    else:
        T = T - mc + mc * fxlx
        print '本月返现金额',mc * fxlx
        fx = fx + mc*fxlx
        print '='*10


T = T*(10.0/14.0)*(1+lx)
print '最终退卡现金额:%.2f' % T
print '消费返',fx