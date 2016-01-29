#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
@author: sunyx
　　代码说明：

　　　　a).ip = lines[i].strip("\n").split("\t") 这个是去掉每行末尾的换行符（也就是"\n"）,然后以制表符（也就是"\t"）分割字符串为字符串数组

　　　　b).proxy_temp = {"http":proxy_host}其中http代表代理的类型，除了http之外还有https，socket等这里就以http为例

　　　　c).urllib.urlopen(url,proxies=proxy) 其中proxies就是代理。以代理模式访问目标网址

　　　　d).socket.setdefaulttimeout(3)设置全局超时时间为3s，也就是说，如果一个请求3s内还没有响应，就结束访问，并返回timeout（超时）
'''
#encoding=utf8
import urllib
import socket
socket.setdefaulttimeout(3)
f = open("proxy")
lines = f.readlines()
proxys = []
for i in range(0,len(lines)):
    ip = lines[i].strip("\n").split("\t")
    proxy_host = "http://"+ip[0]+":"+ip[1]
    proxy_temp = {"http":proxy_host}
    proxys.append(proxy_temp)
url = "http://ip.chinaz.com/getip.aspx"
for proxy in proxys:
    try:
        res = urllib.urlopen(url,proxies=proxy).read()
        print res
    except Exception,e:
        print proxy
        print e
        continue