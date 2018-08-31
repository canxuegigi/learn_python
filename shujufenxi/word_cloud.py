#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import jieba
#还需安装matplotlib，否则会提示模块不存在
from wordcloud import WordCloud

text="李小璐给王思聪买了微博热搜"
result=jieba.cut(text)
#发现结果并不好
print("切分结果:  "+",".join(result))

#人为干预
text="李小璐给王思聪买了微博热搜"
#强调特殊名词
#jieba.suggest_freq(('微博'), True)
#jieba.suggest_freq(('热搜'), True)

#也可以将特殊用词加入用户自定义词典，实现相同的效果，每行一个
jieba.load_userdict("jieba_user_dict.txt")
result=jieba.cut(text)
print("切分结果:  "+",".join(result))

"""
文本清洗
切分之后一些特殊的符号会单独成词，这些词会影响我们之后的分析。可以使用一个标点符号库 stopwords.txt，将切分出来的特殊符号剔除掉。
对于“了”，“的”这样长度为一的词，显然对我们分析文本没有任何帮助。处理的方法为将长度为1的词全部剔除掉。
"""

text = open('调教初唐.txt','r').read()
#读取标点符号库，文件为utf-8，若不指定则可能打开报错
f=open("stopwords.txt","r",encoding='utf-8')
stopwords={}.fromkeys(f.read().split("\n"))
f.close()

#加载用户自定义词典
jieba.load_userdict("jieba_user_dict.txt")
segs=jieba.cut(text)
mytext_list=[]

print("jieba.cut后的返回类型：" , type(segs))

#文本清洗
for seg in segs:
    if seg not in stopwords and seg!=" " and len(seg)!=1:
        mytext_list.append(seg.strip())
cloud_text=",".join(mytext_list)

"""
词云绘制工具wordcloud默认使用的字体是英文的，不包含中文编码，所以才会方框一片。
解决的办法，拷一个中文字体过来，作为指定输出字体。
"""
#background_color="white"
wc = WordCloud(
    background_color="black", #背景颜色
    max_words=250, #显示最大词数
    font_path="FZSTK.TTF",  #使用字体
    min_font_size=15,
    max_font_size=50,
    width=500  #图幅宽度
    )
wc.generate(cloud_text)
wc.to_file("pic.png")