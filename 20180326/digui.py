#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

from bs4 import BeautifulSoup
import requests

r = requests.get('http://www.cnblogs.com/lln7777/archive/2012/03/14/2396164.html')
html = r.text
soup = BeautifulSoup(html,'html.parser')

print html
for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.get_text())


soup.select()




