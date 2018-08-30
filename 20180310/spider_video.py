#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

"""
用于下载'http://www.7mav1.com/视频
用于下载'http://seku.tv/视频

注意：视频的页面地址并不是视频的下载地址，所以有几个步骤

"""

import requests,sys,bs4,re

video_list_new = []
video_dic = {}


# 爬取页数
PAGE_COUNT = 0


def filter_addr_mav(web_url):
    """http://www.7mav1.com/recent/2/"""
    main_video = 'http://www.7mav1.com/'
    #res = requests.get('http://www.7mav1.com/')
    res = requests.get(web_url)
    html = res.text

    """初步过滤，具体根据情况使用正则或者bs4，这里先使用正则"""
    filter_reg_str = 'href="/\d+/'
    filter_reg_compile = re.compile(filter_reg_str)
    filter_list = re.findall(filter_reg_compile, html)

    """拼接视频的访问地址"""
    for i in filter_list:
        video_num = i[7:len(i) - 1]
        video_url = main_video + str(video_num)
        video_list_new.append(video_url)

    print video_list_new

    """获得视频的下载地址，根据实际情况，这里先使用bs4过滤，再通过正则"""
    for i in video_list_new:
        try:
            res = requests.get(i)
            res.raise_for_status()
            noStarchSoup = bs4.BeautifulSoup(res.text,'html.parser')
            elems = noStarchSoup.select('div > video')

            reg_mp4_str = 'src="\S*\.mp4'
            gre_mp4_compile = re.compile(reg_mp4_str)
            video_addr_list = re.findall(gre_mp4_compile, str(elems[0]))
            video_dic[str(i[21:])]=video_addr_list[0][5:]
        except:
            continue

    print '过滤完成......'
    print video_dic

def filter_addr_seku(web_url):
    """http://seku.tv/categories/b6e5bcc1e7b3ee5460e85c4d607d5dda/"""
    """虽然隐藏了地址，但你可以观察试试：
    http://seku.tv/categories/b6e5bcc1e7b3ee5460e85c4d607d5dda/25/
    http://seku.tv/categories/b6e5bcc1e7b3ee5460e85c4d607d5dda/
    """
    main_addr = 'http://seku.tv/categories/b6e5bcc1e7b3ee5460e85c4d607d5dda/'
    #获取当前页

    try:
        page = int(web_url.split('/')[-2])
    except:
        page = 1

    res = requests.get(web_url)
    html = res.text

    filter_reg_str = 'href="http://seku.tv/videos/\d+/\w+'
    filter_reg_compile = re.compile(filter_reg_str)
    filter_list = re.findall(filter_reg_compile, html)

    #循环一页时 临时存储
    tmp_video_dic={}
    #print filter_list
    for i in filter_list:
        video_url = i[6:]+'/'
        tmp_video_dic[str(i.split('/')[4])] = video_url
    print 'tmp_video_dic:',tmp_video_dic
    for i in tmp_video_dic:
        try:
            # print i,tmp_video_dic[i]
            res = requests.get(tmp_video_dic[i])
            res.raise_for_status()
            reg_mp4_str = "video_url: 'function\S*\.mp4/"
            gre_mp4_compile = re.compile(reg_mp4_str)
            video_addr_list = re.findall(gre_mp4_compile, res.text)
            print video_addr_list
            video_addr='http://cdn.dskba.com/contents/videos/'+\
                  video_addr_list[0].split('/')[-4]+'/'+\
                  video_addr_list[0].split('/')[-3]+'/'+\
                  video_addr_list[0].split('/')[-2]
            tmp_video_dic[i] = video_addr
        except:
            continue

    video_dic.update(tmp_video_dic)

    print '第 ',page,' 页过滤完成......'
    page = page + 1
    #TypeError: cannot concatenate 'str' and 'int' objects
    nex_page_addr = main_addr +str(page)+'/'
    #UnboundLocalError: local variable 'page_count' referenced before assignment
    #这里不能修改外层定义的变量，须使用global声明
    global PAGE_COUNT
    PAGE_COUNT = PAGE_COUNT + 1
    print PAGE_COUNT,nex_page_addr
    if PAGE_COUNT < 33:
        filter_addr_seku(nex_page_addr)
    #放这为啥会执行多次知道么，递归啊，我擦
    print '你妹',video_dic,'哈哈'

def down_video(video_dic,save_dir,save_format):
    #TypeError: expected a string or other character buffer object
    #数字和字符串也不能也用+拼接
    f = open('G:\python\\addr_dic.py', 'w')
    for i in video_dic:
        f.write(str(i) + ': ' + str(video_dic[i]))
        f.write('\n')
    f.close()

    for key in video_dic:
    #不能通过保存图片的方式
        #拼接可能报错：UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 0: ordinal not in range(128)
        print '正在保存：',video_dic[key]
        r = requests.get(video_dic[key])
        with open(save_dir+(str(key))+save_format, "wb") as code:
            code.write(r.content)

def main():

    if len(sys.argv) == 2:
        if 'mav' in sys.argv[1]:
            filter_addr_mav(sys.argv[1])
        elif 'seku' in sys.argv[1]:
            filter_addr_seku(sys.argv[1])
        else:
            sys.exit()
        down_video(video_dic,'G:\python\\','.mp4')
    else:
        print 'usage: python spider_video.py web_url'
        sys.exit()

if __name__ == '__main__':
    main()

