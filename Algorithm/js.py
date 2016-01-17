'''
Created on 2016年1月17日

@author: lenovo
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