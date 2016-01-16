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
starturl1 ='http://itjuzi.com/investfirm?invst_state=1&invst_scope=2&page='
starturl2 = 'www.zhihu.com/question/'
question = []
#regex=re.compile(r'(?<=href=\"\/question\/).(?=\/)')


def xieru(url):
    for j in url:
        url2 = j
        #print (url2)
        r2 = urllib.request.urlopen(url2).read().decode('utf-8')
    #print (r2)
    #findhref = re.compile(r'<li>名称:  <a href=\"(.+)?\">')
    #<p> <a href="">泰有投资 </a> </p>
        namef = re.compile(r'<p> <a href=\"\">(.+)?</a> </p>')
    #<li>网址:  <a target="blank" href="http://www.taiyoufund.com">http://www.taiyoufund.com</a> </li>
        urlf = re.compile(r'<li>网址:  <a target=\"blank\" href="(.+)?\">')
    #<li>阶段:  <a href="http://itjuzi.com/investfirm/?invst_state=1">天使初创期</a> </li>
        invstf = re.compile(r'invst_state=(\d)\">')
    #<li>领域:  <a href="http://itjuzi.com/investscope?id=1">互联网</a> , <a href="http://itjuzi.com/investscope?id=2">移动互联网</a> , <a href="http://itjuzi.com/investscope?id=3">医疗健康</a> , <a href="http://itjuzi.com/investscope?id=4">环保能源</a> , <a href="http://itjuzi.com/investscope?id=5">制造业</a> , <a href="http://itjuzi.com/investscope?id=12">硬件</a> </li>
        investscopef= re.compile(r'http://itjuzi.com/investscope\?id=(\d)\">')
    #<li>介绍:  <em>泰有投资成立于2014年，是一家专注于种子投资和天使投资的私募股权投资基金管理公司，由中国青年企业家协会副秘书长孙焱，新东方教育集团董事长俞敏洪，旅美金融家、美国路易斯安那州第一商业银行创始人嵇跃勤，中国青年企业家协会资深副会长、帝恒集团董事长曾钫等知名企业家共同投资组建。积极寻找产业转型升级中的机会，重点关注互联网、电子信息、新材料、节能环保、生物医药等领域。</em></li>
        jieshaof = re.compile(r'<li>介绍:  <em>(.+)?</em></li>')
#<td><a href="http://itjuzi.com/company/25952">信用卡之窗</a></td>
        #companyf = re.compile(u'<a href="http://itjuzi.com/company/[\u4e00-\u9fa5]+</a></td>')
        #print (companyf.findall(r2))
#<td><a href="http://itjuzi.com/investevents?round=9">收购</a></td>
#<td>未透露</td>
#<td><a href="http://itjuzi.com/investevents?scope=12">金融</a></td>
    #print (url2,namef.findall(r2),urlf.findall(r2),invstf.findall(r2),investscopef.findall(r2),jieshaof.findall(r2))
    #juziit.txt
        f=open("juziit.txt","a+")
    #li = (url2,namef.findall(r2),urlf.findall(r2),invstf.findall(r2),investscopef.findall(r2),jieshaof.findall(r2),'\n')
        f.write(url2)
        f.write('\n')
        f.write(str(namef.findall(r2)))
        f.write('\n')
        f.write(str(urlf.findall(r2)))
        f.write('\n')
        f.write(str(invstf.findall(r2)))
        f.write('\n')
        f.write(str(investscopef.findall(r2)))
        f.write('\n')
        f.write(str(jieshaof.findall(r2)))
        f.write('\n')
        f.write('\r')
        f.close()
        time.sleep(2)

secondurl = []

for i in range(1,204):
    print (i)
    urlend1 = str(i)
    starturl = starturl1+urlend1
    r1 = urllib.request.urlopen(starturl).read().decode('utf-8')
#    print (r1)
    findhref = re.compile(r'<li>名称:  <a href=\"(.+)?\">')
    #<li>名称:  <a href="http://itjuzi.com/investfirm/1900">东湖天使基金</a></li>
#    print (findhref.findall(r1))
    secondurl = findhref.findall(r1)
    xieru(secondurl)
    secondurl = []
    time.sleep(1)
#    print (secondurl)
    
if __name__ == '__main__':
    pass