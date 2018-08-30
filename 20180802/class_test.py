#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue


class Students():
    """docstring for Students"""
    def __init__(self, name, age, sex):
        self.name = name
        #私有属性
        self.__age = age
        self.sex = sex

    #析构函数，对象销毁时调用，针对简单脚本就是运行结束后调用
    def __del__(self):
        print '%s调用了析构函数。。。'%self.name
    def show_info(self):
        print 'self.name:%s,self.__age:%s,self.sex:%s' %(self.name,self.__age,self.sex)
    #类外面不能访问
    def __show_info(self):
        print 'self.name:%s,self.__age:%s,self.sex:%s' %(self.name,self.__age,self.sex)




if __name__ == '__main__':
    s1 = Students('canxue','28','F')
    s2 = Students('gigi','40','M')
    #这个print打印的是s1.show_info()的返回值，默认为None
    print s1.show_info()
    #print s1.__show_info()

