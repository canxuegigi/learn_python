#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue
#python 3.x


from urllib import request
import chardet

if __name__ == '__main__':
    var_url = 'https://blog.csdn.net/c406495762'
    var_result = request.urlopen(var_url)
    print(type(var_result))
    print(var_result.geturl())
    print(var_result.info())
    print(var_result.geturl)
    var_byte = var_result.read()
    char_info = chardet.detect(var_byte)
    print(char_info,char_info.get('languag','utf-8'))
    #print(var_byte.decode(char_info.get('encoding','utf-8')))

