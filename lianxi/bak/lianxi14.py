#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
@author: sunyx
'''
def fenjie(n):
    l = []
    for i in range(2,n+1):
        while n != i:
            if n % i == 0:
                l.append(i)
                n = n /i
            else:
                break
    l.append(n)
    return l
            
#print fenjie(1000)


'''
def factor(N, q_factor=None):
    if q_factor is None:
        q_factor = [];

    isPrime = True; # Initialize isPrime to False.
    
    for x in range(2, N):
        if N % x == 0:
            factor1 = x;
            factor2 = N//x; 
            print(N, 'equals', factor1, '*', factor2);
            print('Further factorization over',factor1);
            factor(factor1, q_factor);
            print('Further factorization over',factor2);
            factor(factor2, q_factor);
            isPrime = False
            break  
    if isPrime is True:
        print(N, 'is a prime number');
        q_factor.append(N);

    return isPrime;


N = int(input("Please input a positive integer for factorization(>=2):"))

if N<2:
    print("N shall be not less than 2");
    exit

q_factor=[]
isPrime = factor(N,q_factor)    
    
if isPrime is False:
    print(N, " is factorized into:", q_factor)
else:
    print(N, " is a prime number by itself!")
'''

def fenjies(n,lss = None):
    if lss == None:
        lss = []
    isf = True
    for i in range(2,n):
        if n % i == 0:
            f1 = i
            f2 = n // i
            #print f1,f2
            fenjies(f1,lss)
            fenjies(f2,lss)
            isf = False
            break
    if isf is True:
        print '素数',n
        lss.append(n)
    return isf,lss


print fenjies(32312342)[1]
    