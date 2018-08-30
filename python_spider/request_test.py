#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import requests
kw = {
    "wd":'郑靖'
}


auth_info = {
    "password_name":'郑靖',
    "password_pwd":''
}

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

rsp = requests.get('https://www.12306.cn',headers=headers)
rsp.encoding = 'utf-8'
# print(rsp.text)
print(type(rsp.cookies))
print(requests.utils.dict_from_cookiejar(rsp.cookies))

