#!/usr/bin/evn python
#encoding=utf-8
#Author:can


from lxml import etree

for i in etree.parse("./books.xml").xpath('book/year'):
    print('tag:%s,text:%s' %(i.tag,i.text))