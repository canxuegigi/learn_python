#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue


class A():
    def __init__(self):
        print "A"

class B(A):
    pass
    # def __init__(self):
    #     print "B"

class C(A):
    def __init__(self):
        print "C"

class D(B,C):
    pass
    # def __init__(self):
    #     print "D"

d = D()