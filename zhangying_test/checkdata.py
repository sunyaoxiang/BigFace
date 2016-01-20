#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
@author: sunyx
'''
import requests
import json
import re
#import ssl,socket,time,OpenSSL 

#context = OpenSSL.SSL.Context(ssl.PROTOCOL_SSLv23)
#context.load_cert_chain(certfile='www.fencard.com.pfx')


result= []
of = open('datatext.txt','r')
fr = of.readlines()
fs = []
for line in fr:
    line = line.strip(',\n').strip('(').strip(')').split(',')
    fs.append(line)
#print 'fs:',fs

for fd in fs:
    login_account = fd[0]
    login_pwd = fd[1]
    #print 'login_account:',login_account,'login_pwd:',login_pwd
    url = 'https://www.fencard.com/serviceoperate.svc/logincommit';
    header = {'Accept-Encoding': 'gzip,deflate',
              'Content-Type': 'application/json;charset=UTF-8',
              'Host': 'www.fencard.com',
              'Connection': 'Keep-Alive',
              'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)'
              }
    jsondata = {'account':login_account,
            'password':login_pwd,
            'sp':{"cv":"1.0","from":"android","iv":"1","m":"GT-I9505","o":"KOT49H","v":"4.4.2"},
            'Accept-Encoding': 'gzip,deflate',
            'Content-Type': 'application/json;charset=UTF-8',
            'Host': 'www.fencard.com',
            'Connection': 'Keep-Alive',
            'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)'}
    #request.add_header('Content-Type': 'application/json;charset=UTF-8')
    rs = requests.post(url,json=jsondata)
    #print jsondata
    rf = rs.text
    #print rf
    #print rf.decode('utf-8')
    isrf = re.findall(u'\"msg\":\"成功\",\"status\":2000',rf)
    if bool(isrf):
        print login_account,'登录成功'
    else:
        print login_account,'登录失败'

of.close()