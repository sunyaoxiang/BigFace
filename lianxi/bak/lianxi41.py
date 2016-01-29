#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
模仿静态变量的用法。
@author: sunyx
'''

def varfunc():
    var = 0
    print 'var = %d' % var
    var += 1
if __name__ == '__main__':
    for i in range(3):
        varfunc()
        
class sunyx:
    basevare = 5
    def addn(self):
        self.basevare += 1
        print self.basevare

for i in range(0,4):
    sunyx().addn()