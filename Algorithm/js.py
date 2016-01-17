# -*- coding: utf-8 -*-
'''
知乎上的，只能用Python2.7,3.0不支持xrange！
'''

def d(n):
    s = 0
    for i in xrange(1, int(n**0.5)+1):
        s += n/i*i
        
    i = int(n**0.5)+1
    for j in xrange(n/i, 0, -1):
        s += j * ((i+n/j)*(n/j-i+1)/2)
        i = n/j+1
    return s

print(d(10**12))