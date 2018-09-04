#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue
"""
爬取字幕组的资源列表
"""
import requests,pymysql,re,time
import conn_manage
from bs4 import BeautifulSoup

def get_page_num(url):
    rsp = requests.get(url)
    rsp.encoding = 'utf-8'
    soup = BeautifulSoup(rsp.text, 'lxml')
    page_list = soup.select('.pages')
    page_str = r'\.\.\.\d+'
    page_regex = re.compile(page_str)
    match_result = page_regex.search(str(page_list[0]))
    max_page = str(match_result.group()).replace('...','')
    return int(max_page)

def loop_page_and_save(url,max_page):

    mysql_conn =  conn_manage.get_mysql_conn()
    mysql_cursor = mysql_conn.cursor()

    truncate_sql = "TRUNCATE spider.zimuzu_resource_list;"
    mysql_cursor.execute(truncate_sql)

    insert_sql = "insert into spider.zimuzu_resource_list(chinese_name,english_name,type,release_time,url,channel,country,update_time) VALUE (%s,%s,%s,%s,%s,%s,%s,%s)"

    for i in range(max_page):
        current_url = url+'?page='+str(i+1)
        print("current_url:",current_url)
        rsp = requests.get(current_url)
        rsp.encoding = 'utf-8'
        soup = BeautifulSoup(rsp.text, 'lxml')
        resource_list = soup.select('.resource-list .clearfix .fl-info')
        #返回的是列表，但元素并不是字符串对象，而是特定对象，所以每个元素还有其自己对应的属性和方法
        for resource_info in resource_list:
            try:
                resource_url = 'http://www.zimuzu.io'+resource_info.select('dt a')[0].attrs.get('href')
                update_time = resource_info.select('dt span')[0].attrs.get('time')
                update_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(update_time)))
                channel = resource_info.select('dt a strong')[0].getText()

                #地区
                begin_position = str(resource_info.select('dt .f14 a')[0].getText()).find('【')+1
                end_position = str(resource_info.select('dt .f14 a')[0].getText()).find('】')
                country = str(resource_info.select('dt .f14 a')[0].getText())[begin_position:end_position]

                #中文名
                begin_position = str(resource_info.select('dt .f14 a')[0].getText()).find('《')+1
                end_position = str(resource_info.select('dt .f14 a')[0].getText()).find('》')
                chinese_name = str(resource_info.select('dt .f14 a')[0].getText())[begin_position:end_position]

                #英文名
                begin_position = str(resource_info.select('dt .f14 a')[0].getText()).find('(')+1
                end_position = str(resource_info.select('dt .f14 a')[0].getText()).find(')')
                english_name = str(resource_info.select('dt .f14 a')[0].getText())[begin_position:end_position]

                #年份
                resource_year = str(resource_info.select('dt .f14 a')[0].getText())[-4:]

                begin_position = str(resource_info.select('dd')).find('【类型】 ')
                end_position = str(resource_info.select('dd')).find('<',begin_position)
                resource_type = str(resource_info.select('dd'))[begin_position:end_position].strip()[4:].strip()

                print(chinese_name,english_name,resource_type,resource_year,url,channel,country,update_time)

                mysql_cursor.execute(insert_sql,(chinese_name,english_name,resource_type,resource_year,resource_url,channel,country,update_time))
                #需要手动提交
                mysql_conn.commit()

            except:
                continue

    mysql_cursor.close()
    conn_manage.close_conn(mysql_conn)

def main():
    base_url = 'http://www.zimuzu.io/resourcelist'
    max_page = get_page_num(base_url)
    print('max_page:',max_page)
    loop_page_and_save(base_url,max_page)


if __name__ == '__main__':
    main()
