#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import requests,sys,bs4,urllib,re

"""
video_address = {'10321': 'http://www.7mav1.com/file/10321/2/fc24036f6c0e02bbb57d/1520691737/mp4/10321.mp4'}
for key in video_address:
    r = requests.get(video_address[key])
    with open('G:\python\%s.mp4' % (str(key)), "wb") as code:
        code.write(r.content)
"""


#video_list_new = [1,2,]
video_list_new = []
video_dic = {'a':'fdsfds','b':'fdsfds'}
a = 0

#res = requests.get('http://seku.tv/videos/3930/9cf67fa257520034ef1644bcefb705d9/')
#html = res.text
#print html

# def test_global():
#     video_list_new
#     print video_dic
#     video_list_new = video_list_new.append([1,2,5])
#     global a
#     a=a+1
#     print a
#
# test_global()

# def main():
#     test_global()
#
# if __name__ == '__main__':
#     main()

"""
filter_reg_str = 'href="http://seku.tv/videos/\d+/\w+'
filter_reg_compile = re.compile(filter_reg_str)
filter_list = re.findall(filter_reg_compile, html)
print  filter_list[0], filter_list[0][6:]+'/'
for i in filter_list:
    video_url = i[6:]+'/'
    video_dic[str(i.split('/')[4])] = video_url
"""



a={'a':1,'b':1}
b={'b':1}

f = open('G:\python\\addr_dic.py', 'a')
for i in a:
    print str(i),a[i]
    f.write(str(i)+'→'+str(a[i]))
    f.write('\n')
f.close()

