'''
195132894
入群题：求1<=i<=10**12范围内所有d(i)的和的末12位，d(i)表示i的正约数的和，i为整数

'''
import datetime
starttime = datetime.datetime.now()

def d(n):
    s = 0
    m = int(n**0.5)
    for i in range(1,m):
        s = s + (((1+i)*i)/2) + (((1+n//i)*(n//i))/2)
        #print(i,s)
    s = s + (((1+m)*m)/2)
    for i in range(1,m):
        if ((n//i)-2*m+i > 0):
            s = s + ((n//i)-2*m+i)*i
            #print(i,((n//i)-2*m+i)*i)
        else:
            break;
    return int(s)

print(d(10**12))

#822467033425 357340138978 right
#822467033425 120044515328
'''
def d(n):
    s = 0
    for i in range(1,int(n**0.5)+1):
        s = s + (n//i)*i
    i = int(n**0.5)+1
    #print ('i:',i)
    for j in range(1,i-1):
        #k = n//j
        #length = k-i+1
        #print('j:',j,'k:',k,'j*k:',j*k,'length:',length,'count',(i+k)*length*0.5,'i:',i)
        s = s+(i+n//j)*(n//j-i+1)/2
    return s
print(int(d(10**9)))

#822467033425 357340138978
#822467033425 366736699392
#822467033425 120044515328


endtime = datetime.datetime.now()
print ('耗时',(endtime - starttime).seconds)
'''

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
'''