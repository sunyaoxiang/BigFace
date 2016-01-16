'''
Created on 2014年3月28日
http://itjuzi.com/investfirm?invst_scope=2&page=1
@author: Administrator
'''

#!/usr/bin/env python3
import urllib.request
import re
import time


#href=\"\/question\/30326597\/answer\/47628560
starturl1 ='http://itjuzi.com/investor?invst_scope=2&page='
starturl2 = 'www.zhihu.com/question/'
question = []
#regex=re.compile(r'(?<=href=\"\/question\/).(?=\/)')


def xieru(url):
    for j in url:
        url2 = j
        #print (url2)
        r2 = urllib.request.urlopen(url2).read().decode('utf-8')
        #print (r2)
        namef = re.compile(r'<meta name=\"Keywords\" content=\"(.+)?,IT桔子\" />')
        #print (namef.findall(r2))
#<li> 职位: <a href="http://itjuzi.com/investfirm/1862">耀途资本</a> 创始合伙人 </li>
        gsf = re.compile(r'<li>职位:  <a href=\"(.+)?\">')
        #print (gsf.findall(r2))
        #<li> 微博: <a href="http://weibo.com/u/1909839954">http://weibo.com/u/1909839954</a>
        weibof = re.compile(r'<li>微博:  <a href=\"(.+)?\">')
        
        jieshaof = re.compile(r'<li>介绍:  <em>(.+)?</em></li>')
        
        addressf = re.compile(r'</a>,<em>(.+)?</em> </li>')
        
        tzlyf = re.compile(r'http://itjuzi.com/investscope\?id=(\d)\">')
        
        #print (tzlyf.findall(r2))
        f=open("juziittzr.txt","a+")
        
        f.write('\r\n')
        f.write(str(namef.findall(r2)))
        f.write('\r\n')
        f.write(url2)
        f.write('\r\n')
        f.write(str(gsf.findall(r2)))
        f.write('\r\n')
        f.write(str(weibof.findall(r2)))
        f.write('\r\n')
        f.write(str(jieshaof.findall(r2)))
        f.write('\r\n')
        f.write(str(addressf.findall(r2)))
        f.write('\r\n')
        f.write(str(tzlyf.findall(r2)))
        f.write('\r\n')
        f.write('\r\n')
        f.close()
        time.sleep(2)

secondurl = []

for i in range(1,58):
    print (i)
    urlend1 = str(i)
    starturl = starturl1+urlend1
    r1 = urllib.request.urlopen(starturl).read().decode('utf-8')
#    print (r1)
#<a class="pull-left" href="http://itjuzi.com/investor/1367">
    findhref = re.compile(r'<h4 class=\"media-heading\"> <a class=\"media-tit\" href=\"(.+)?\">')
    #<li>名称:  <a href="http://itjuzi.com/investfirm/1900">东湖天使基金</a></li>
    #print (findhref.findall(r1))
    secondurl = findhref.findall(r1)
    xieru(secondurl)
    secondurl = []
    time.sleep(1)
    #print (secondurl)
    
if __name__ == '__main__':
    pass