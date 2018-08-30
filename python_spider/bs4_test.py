#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue



import  requests
from bs4 import BeautifulSoup

rsp = requests.get("http://www.baidu.com")
rsp.encoding = 'utf-8'
soup = BeautifulSoup(rsp.text,'lxml')

print(soup.get_text)
