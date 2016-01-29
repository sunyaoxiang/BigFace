#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
@author: sunyx
　　代码说明：

　　　　a).这里我们使用的urllib2模块，因为，这个请求有点特殊，服务器会验证请求中的header（如有疑问，可参考http的相关资料）

　　　　b).urllib2与urllib的区别在于，urllib2发送请求的时候可携带参数（我现在只用到这点区别）

　　　　c).open()用于打开文件，第一个参数是文件的路径可以填绝对路径，例如E:\\proxy（"\"在编程中是特殊字符，要用"\\"代表实际的"\"）。也可以是相对路径，比　　　　如"../src/proxy"，就是文件相对于代码的位置。第二个参数"w"，代表打开文件的权限，w代表写权限，r代表读权限。这个在很多系统中都通用。比如，linux等

　　　　d).for循环，如果之前学过java或者其他高级语言，可能不太习惯，因为他们用的是for(;;)这样的。python中的for循环，in 表示X的取值，按顺序取到in后面的参数

　特别注意：别忘了for语句后面的冒号（":"）

　　　　c).range函数，代表生成一系列数，如果range(0,6,1)，意思就是从0开始，到6结束（不包括6），每次增加1（也就是步长为1），生成一个数组，结果就是[0, 1, 2, 3, 4, 5]

　　　　e).f.write()就是往文件里面写数据，如果打开文件的时候，没有"w"权限，则无法写入。
'''
#encoding=utf8
import urllib2
import BeautifulSoup

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

url = 'http://www.xicidaili.com/nn/1'
req = urllib2.Request(url,headers=header)
res = urllib2.urlopen(req).read()

soup = BeautifulSoup.BeautifulSoup(res)
ips = soup.findAll('tr')
f = open("proxy","w")

for x in range(1,len(ips)):
    ip = ips[x]
    tds = ip.findAll("td")
    ip_temp = tds[2].contents[0]+"\t"+tds[3].contents[0]+"\n"
    #print tds[2].contents[0]+"\t"+tds[3].contents[0]
    f.write(ip_temp)